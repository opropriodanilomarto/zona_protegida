"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django.urls import include, path

from . import views

app_name = "zp"

urlpatterns = [
    path("", views.home, name="home"),
    path("customers/", include("zp.customers.urls", namespace="customers")),
    path("accounts/", include("zp.accounts.urls", namespace="accounts")),
]
