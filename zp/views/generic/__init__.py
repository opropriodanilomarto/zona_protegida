"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>

Class-based views (CBV) from the django.views.generic package with the LoginRequeredMixin mixin implemented.
"""

from .base import TemplateView


__all__ = [
    "TemplateView",
]
