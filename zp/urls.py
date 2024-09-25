from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("service/<slug:service>/", views.list_services, name="list_services"),
]
