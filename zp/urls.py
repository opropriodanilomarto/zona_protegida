"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django.urls import include, path

from . import views

app_name = "zp"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("service/<slug:service>/", views.ServiceList.as_view(), name="service_list"),
    path("accounts/", include("zp.accounts.urls")),
]
