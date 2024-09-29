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
    path("service/<slug:service>/", views.ListView.as_view(), name="list_by_service"),
    path("<slug:slug>/", views.DetailView.as_view(), name="detail"),
    path("<slug:slug>/update/", views.UpdateView.as_view(), name="update"),
    path("<slug:slug>/delete/", views.DeleteView.as_view(), name="delete"),
]
