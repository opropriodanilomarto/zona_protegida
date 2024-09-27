import re

from typing import Any

from .generic import TemplateView


class Index(TemplateView):
    template_name = "zp/index.html"


class ServiceList(TemplateView):
    template_name = "zp/service_list.html"

    def get_service(self) -> str:
        return re.sub("-", " ", self.kwargs.get("service"))

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        if "service" not in kwargs:
            kwargs["service"] = self.get_service()
        return super().get_context_data(**kwargs)
