"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from zp.forms import AddressForm

from zp.models import Address
from .forms import CustomerForm
from .models import Customer


@login_required
def customer_list(request: HttpRequest, service_type: str | None = None) -> HttpResponse:
    template_name = "zp/customers/customer_list.html"
    customers = Customer.objects.filter(deleted=False)

    if service_type:
        customers = customers.filter(service_type=service_type)

    context = {"pg": "customers", "service_type": service_type, "customers": customers}
    return render(request, template_name, context)


@login_required
def customer_detail(request: HttpRequest, slug: str) -> HttpResponse:
    template_name = "zp/customers/customer_detail.html"
    customer = get_object_or_404(Customer.objects.filter(deleted=False), slug=slug)
    context = {"pg": "customers", "customer": customer}
    return render(request, template_name, context)


@login_required
def customer_create(request: HttpRequest) -> HttpResponse:
    template_name = "zp/customers/customer_create.html"
    form = CustomerForm(request.POST or None)

    if request.method != "POST" or not form.is_valid():
        context = {"pg": "customers", "form": form}
        return render(request, template_name, context)

    customer = form.save(commit=False)
    customer.employee = request.user
    customer.address = Address.objects.create()
    customer.save()

    return redirect(customer.get_absolute_url_to_update())


@login_required
def customer_update(request: HttpRequest, slug: str) -> HttpResponse:
    template_name = "zp/customers/customer_update.html"
    customer = get_object_or_404(Customer.objects.filter(deleted=False), slug=slug)
    form = CustomerForm(request.POST or None, instance=customer)
    address_form = AddressForm(request.POST or None, instance=customer.address)

    if request.method != "POST" or not form.is_valid() or not address_form.is_valid():
        context = {"pg": "customers", "form": form, "address_form": address_form, "customer": customer}
        return render(request, template_name, context)

    address_form.save()
    customer = form.save()

    return redirect(customer.get_absolute_url())


@login_required
def customer_delete(request: HttpRequest, slug: str) -> HttpResponse:
    template_name = "zp/customers/customer_detail.html"
    customer = get_object_or_404(Customer.objects.filter(deleted=False), slug=slug)

    if request.method != "POST":
        context = {"pg": "customers", "customer": customer, "delete": True}
        return render(request, template_name, context)

    customer.deleted = True
    customer.save()
    return redirect(reverse_lazy("zp:customers:customer_list", kwargs={"service_type": customer.service_type}))
