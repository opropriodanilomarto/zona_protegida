"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>

Class-based views (CBV) from the django.views.generic.base module with the LoginRequeredMixin mixin implemented.
"""

from typing import Any

from django.views.generic.base import TemplateView as Tv, ContextMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class ResourceMixin(ContextMixin):
    resource: str | None = None

    def get_resource(self) -> str | None:
        if not self.resource:
            self.resource = self.kwargs.get("resource")
        return self.resource

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        if "resource" not in kwargs:
            kwargs["resource"] = self.get_resource()
        return super().get_context_data(**kwargs)


class TemplateView(LoginRequiredMixin, Tv):
    pass
