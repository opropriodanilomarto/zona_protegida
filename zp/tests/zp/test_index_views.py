from django.test import TestCase
from django.urls import reverse

from zp.tests.auth import SuperUser


class TestCaseUserMakesGetRequestHomePageNotAuthenticated(TestCase):
    """
    Test case the user makes a GET request to the home page when not authenticated
    """

    def test_status_code_is_302(self) -> None:
        r = self.client.get(reverse("zp:index"))
        self.assertEqual(r.status_code, 302)

    def test_user_directed_login_page(self) -> None:
        r = self.client.get(reverse("zp:index"))
        self.assertRedirects(r, "/accounts/login/?next=/")


class TestCaseSuperuserMakesGetRequestHomePageAlreadyAuthenticated(SuperUser):
    """
    Test case the superuser makes a GET request to the home page when he is already authenticated.
    """

    def test_status_code_is_200(self) -> None:
        r = self.client.get(reverse("zp:index"))
        self.assertEqual(r.status_code, 200)

    def test_template_name_used_is_index(self) -> None:
        r = self.client.get(reverse("zp:index"))
        self.assertTemplateUsed(r, "zp/index.html")
