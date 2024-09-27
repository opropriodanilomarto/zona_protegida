"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django.urls import path
from . import views


app_name = "customers"

urlpatterns = [
    path("create/", views.CreateView.as_view(), name="create"),
    path("", views.ListView.as_view(), name="list"),
    path("<slug:customer>/", views.DetailView.as_view(), name="detail"),
    path("<slug:customer>/update/", views.UpdateView.as_view(), name="update"),
    path("<slug:customer>/delete/", views.ListView.as_view(), name="delete"),
]
