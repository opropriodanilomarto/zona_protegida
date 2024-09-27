"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from typing import Any

from django.views.generic.base import ContextMixin
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import get_object_or_404

from zp.views import generic as g
from .models import Person, PersonQuerySet


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


class CustomerMixin(SingleObjectMixin):
    def get_object(self, queryset: Person | None = None) -> PersonQuerySet:
        return get_object_or_404(Person, slug=self.kwargs.get("customer"))


class CreateView(ServiceMixin, g.TemplateView):
    template_name = "customers/form.html"


class ListView(ServiceMixin, g.ListView):
    template_name = "customers/list.html"
    queryset = Person.objects.all()
    context_object_name = "customers"

    def get_queryset(self) -> PersonQuerySet:
        return self.queryset.filter(type_service=self.get_service()).only("name")


class DetailView(ServiceMixin, CustomerMixin, g.DetailView):
    template_name = "customers/detail.html"
    queryset = Person.objects.all()
    context_object_name = "customer"


class UpdateView(ServiceMixin, CustomerMixin, g.TemplateView):
    template_name = "customers/form.html"


class DeleteView(ServiceMixin, CustomerMixin, g.TemplateView):
    template_name = "customers/Delete.html"
