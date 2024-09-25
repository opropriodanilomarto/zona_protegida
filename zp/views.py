import re
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "zp/index.html")


def list_services(request: HttpRequest, service: str) -> HttpResponse:
    service = re.sub("-", " ", service)
    return render(request, "zp/list_services.html", {"service": service})
