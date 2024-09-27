"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>

Class-based views (CBV) from the django.views.generic.edit module with the LoginRequeredMixin mixin implemented.
"""

from django.views.generic.edit import UpdateView as Uv, CreateView as Cv
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateView(LoginRequiredMixin, Cv):
    pass


class UpdateView(LoginRequiredMixin, Uv):
    pass
