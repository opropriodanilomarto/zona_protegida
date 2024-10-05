"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django import forms
from .models import Alarm, Camera


class AlarmForm(forms.ModelForm):
    class Meta:
        model = Alarm
        fields = ("description",)


class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ("description",)
