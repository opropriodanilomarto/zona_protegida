from django.test import TestCase
from django.urls import reverse


class TestGetRequestToListServicePath(TestCase):
    def test_status_code_is_200(self) -> None:
        r = self.client.get(reverse("list_services", kwargs={"service": "only-alarms"}))
        self.assertEqual(r.status_code, 200)

    def test_template_name_used_is_index(self) -> None:
        r = self.client.get(reverse("list_services", kwargs={"service": "only-alarms"}))
        self.assertTemplateUsed(r, "zp/list_services.html")

    def test_service_keyword_in_context_response(self) -> None:
        r = self.client.get(reverse("list_services", kwargs={"service": "only-alarms"}))
        self.assertIn("service", r.context)

    def test_service_keyword_value_of_context(self) -> None:
        r = self.client.get(reverse("list_services", kwargs={"service": "only-alarms"}))
        self.assertEqual(r.context["service"], "only alarms")
