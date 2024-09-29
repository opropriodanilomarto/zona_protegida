"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>

Class-based views (CBV) from the django.views.generic.base module with the LoginRequeredMixin mixin implemented.
"""

from django.views.generic.base import TemplateView as Tv
from django.contrib.auth.mixins import LoginRequiredMixin


class TemplateView(LoginRequiredMixin, Tv):
    pass
