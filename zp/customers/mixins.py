"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from typing import Any

from django.views.generic.base import ContextMixin


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
