from django.test import SimpleTestCase
from django.urls import reverse


class TestGetRequestToRootPath(SimpleTestCase):
    def test_status_code_is_200(self) -> None:
        r = self.client.get(reverse("index"))
        self.assertEqual(r.status_code, 200)

    def test_template_name_used_is_index(self) -> None:
        r = self.client.get(reverse("index"))
        self.assertTemplateUsed(r, "zp/index.html")
