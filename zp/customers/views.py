"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from zp.views.generic import ListView, CreateView, UpdateView, DetailView

from .models import Person, PersonQuerySet
from .forms import CreatePersonForm, UpdatePersonForm, DeletePersonForm
from .mixins import CustomerContextMixin, ServiceMixin


class CreateView(CreateView, CustomerContextMixin, ServiceMixin):
    template_name = "zp/customers/create.html"
    form_class = CreatePersonForm

    def get_success_url(self) -> str:
        return self.object.get_absolute_url_to_update()

    def form_valid(self, form) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.employee = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ListView(ListView, CustomerContextMixin, ServiceMixin):
    template_name = "zp/customers/list.html"
    queryset = Person.objects.all().filter(deleted=False)
    context_object_name = "customers"

    def get_queryset(self) -> PersonQuerySet:
        service = self.get_service()
        if service:
            self.queryset = self.queryset.filter(type_service=service)
        return self.queryset.only("name", "type_service")


class DetailView(DetailView, CustomerContextMixin):
    template_name = "zp/customers/detail.html"
    queryset = Person.objects.all()
    context_object_name = "customer"


class UpdateView(UpdateView, CustomerContextMixin):
    template_name = "zp/customers/update.html"
    queryset = Person.objects.all()
    context_object_name = "customer"
    form_class = UpdatePersonForm


class DeleteView(UpdateView, CustomerContextMixin):
    template_name = "zp/customers/delete.html"
    queryset = Person.objects.all()
    context_object_name = "customer"
    form_class = DeletePersonForm
    success_url = "zp:customers:list"

    def post(self, request, *args, **kwargs) -> HttpResponse:
        super().post(request, *args, **kwargs)
        self.object.deleted = True
        self.object.save()
        return redirect(reverse_lazy(self.success_url))
