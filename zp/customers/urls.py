"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django.urls import path
from . import views


app_name = "customers"

urlpatterns = [
    path("", views.customer_list, name="customer_list"),
    path("service_type/<slug:service_type>/", views.customer_list, name="customer_list"),
    path("c/create/", views.customer_create, name="customer_create"),
    path("<slug:slug>/", views.customer_detail, name="customer_detail"),
    path("<slug:slug>/update/", views.customer_update, name="customer_update"),
    path("<slug:slug>/delete/", views.customer_delete, name="customer_delete"),
]
