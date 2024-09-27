from django.urls import path, include
from . import views


app_name = "zp"

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("service/<slug:service>/", views.ServiceList.as_view(), name="service_list"),
    path("accounts/", include("zp.accounts.urls")),
]
