"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("name", "service_type", "note")
