"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            "street",
            "number",
            "complement",
            "neighborhood",
            "city",
            "state",
            "country",
            "zip_code",
        )
