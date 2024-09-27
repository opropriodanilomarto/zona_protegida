"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from .generic import TemplateView


class Index(TemplateView):
    template_name = "zp/index.html"
