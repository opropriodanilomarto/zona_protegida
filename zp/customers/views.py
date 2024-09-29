"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from typing import Any

from django.views.generic.base import ContextMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy

from zp.views import generic as g
from .models import Person, PersonQuerySet
from .forms import CreatePersonForm, UpdatePersonForm, DeletePersonForm


class CustomerContextMixin:
    extra_context = {"pg": "customers"}


class ServiceMixin(ContextMixin):
    service: str = None

    def get_service(self) -> str:
        if not self.service:
            self.service = self.kwargs.get("service")
        return self.service

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        if "service" not in kwargs:
            kwargs["service"] = self.get_service()
        return super().get_context_data(**kwargs)


class CreateView(CustomerContextMixin, ServiceMixin, g.CreateView):
    template_name = "customers/create.html"
    form_class = CreatePersonForm

    def get_success_url(self) -> str:
        return self.object.get_absolute_url_to_update()

    def form_valid(self, form) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.employee = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ListView(CustomerContextMixin, ServiceMixin, g.ListView):
    template_name = "customers/list.html"
    queryset = Person.objects.all().filter(deleted=False)
    context_object_name = "customers"

    def get_queryset(self) -> PersonQuerySet:
        service = self.get_service()
        if service:
            self.queryset = self.queryset.filter(type_service=service)
        return self.queryset.only("name", "type_service")


class DetailView(CustomerContextMixin, g.DetailView):
    template_name = "customers/detail.html"
    queryset = Person.objects.all()
    context_object_name = "customer"


class UpdateView(CustomerContextMixin, g.UpdateView):
    template_name = "customers/update.html"
    queryset = Person.objects.all()
    context_object_name = "customer"
    form_class = UpdatePersonForm


class DeleteView(CustomerContextMixin, g.UpdateView):
    template_name = "customers/delete.html"
    queryset = Person.objects.all()
    context_object_name = "customer"
    form_class = DeletePersonForm
    success_url = "zp:customers:list"

    def post(self, request, *args, **kwargs) -> HttpResponse:
        super().post(request, *args, **kwargs)
        self.object.deleted = True
        self.object.save()
        return redirect(reverse_lazy("zp:customers:list"))
