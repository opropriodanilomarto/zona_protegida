from django.test import TestCase
from django.urls import reverse

from zp.tests.auth import SuperUser


class TestCaseUserMakesGetRequestServicePageNotAuthenticated(TestCase):
    """
    Test case the user makes a GET request to the home page when not authenticated
    """

    def setUp(self) -> None:
        self.service_list = ["only-alarms", "only-cameras", "alarms-and-cameras"]

    def test_status_code_is_302(self) -> None:
        for service in self.service_list:
            r = self.client.get(reverse("zp:service_list", kwargs={"service": service}))
            self.assertEqual(r.status_code, 302)

    def test_user_directed_login_page(self) -> None:
        for service in self.service_list:
            r = self.client.get(reverse("zp:service_list", kwargs={"service": service}))
            self.assertRedirects(r, f"/accounts/login/?next=/service/{service}/")


class TestCaseSuperuserMakesGetRequestServicePageAlreadyAuthenticated(SuperUser):
    """
    Test case the superuser makes a GET request to the home page when he is already authenticated.
    """

    def setUp(self) -> None:
        super().setUp()
        self.service_list = ["only-alarms", "only-cameras", "alarms-and-cameras"]

    def test_status_code_is_200(self) -> None:
        for service in self.service_list:
            r = self.client.get(reverse("zp:service_list", kwargs={"service": service}))
            self.assertEqual(r.status_code, 200)

    def test_template_name_used_is_service_list(self) -> None:
        for service in self.service_list:
            r = self.client.get(reverse("zp:service_list", kwargs={"service": service}))
            self.assertTemplateUsed(r, "zp/service_list.html")


#     def test_service_keyword_in_context_response(self) -> None:
#         for service in self.service_list:
#             r = self.client.get(reverse("zp:service_list", kwargs={"service": service}))
#             self.assertIn("service", r.context)

#     def test_service_keyword_value_of_context(self) -> None:
#         for service in self.service_list:
#             r = self.client.get(reverse("zp:service_list", kwargs={"service": service}))
#             self.assertEqual(r.context["service"], re.sub("-", " ", service))
