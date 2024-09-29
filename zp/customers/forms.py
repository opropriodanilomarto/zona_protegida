"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django import forms
from .models import Person


class CreatePersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("name", "type_person", "type_service")


class UpdatePersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("name", "type_person", "type_service", "note")


class DeletePersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("name", "type_person", "type_service", "note")
        # fields = ("deleted")
