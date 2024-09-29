"""
All data used in the tests was obtained from the people generator on the 4devs website
site: https://www.4devs.com.br/gerador_de_pessoas
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from zp.people.models import Person
from django.utils.text import slugify


UserModel = get_user_model()


class TestCasePersonModel(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.employee = UserModel.objects.create(username="user@test", password="user@pass")

    def test_person_created(self) -> None:
        person = {
            "employee": self.employee,
            "name": "Matheus Levi Luan Bernardes",
            "type_person": Person.NP,
            "type_service": Person.OA,
        }
        p = Person.objects.create(**person)

        self.assertEqual(p.slug, slugify(p.name))
        self.assertEqual(p.query, f"{p.name} {p.type_person} {p.type_service} {p.employee}")
