from django.test import TestCase
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class SuperUser(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.credentials = {"username": "superuser", "password": "superuser@zp"}

        UserModel.objects.create_superuser(**cls.credentials)

    def setUp(self) -> None:
        self.client.login(**self.credentials)
