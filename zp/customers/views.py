"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from zp.forms import AddressForm
from zp.services.models import Alarm, Camera
from zp.services.forms import AlarmForm, CameraForm
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
    template_name = "zp/customers/customer_form.html"

    def forms_is_valid(*args):
        return all(args)

    alarm_formset_factory = inlineformset_factory(Customer, Alarm, form=AlarmForm, extra=1, can_delete=False)
    camera_formset_factory = inlineformset_factory(Customer, Camera, form=CameraForm, extra=1, can_delete=False)

    address_form = AddressForm(request.POST or None)
    customer_form = CustomerForm(request.POST or None)
    alarm_formset = alarm_formset_factory(request.POST or None)
    camera_formset = camera_formset_factory(request.POST or None)

    if request.method == "GET" or not forms_is_valid(
        address_form.is_valid(), customer_form.is_valid(), alarm_formset.is_valid(), camera_formset.is_valid()
    ):
        context = {
            "pg": "customers",
            "address_form": address_form,
            "customer_form": customer_form,
            "alarm_formset": alarm_formset,
            "camera_formset": camera_formset,
        }
        return render(request, template_name, context)

    address = address_form.save()

    customer = customer_form.save(commit=False)
    customer.employee = request.user
    customer.address = address
    customer.save()

    alarm_formset.instance = customer
    alarm_formset.save()

    camera_formset.instance = customer
    camera_formset.save()

    return redirect(customer.get_absolute_url_to_update())


@login_required
def customer_update(request: HttpRequest, slug: str) -> HttpResponse:
    template_name = "zp/customers/customer_form.html"
    customer = get_object_or_404(Customer.objects.filter(deleted=False), slug=slug)

    def forms_is_valid(*args):
        return all(args)

    alarm_formset_factory = inlineformset_factory(Customer, Alarm, form=AlarmForm, extra=1, can_delete=False)
    camera_formset_factory = inlineformset_factory(Customer, Camera, form=CameraForm, extra=1, can_delete=False)

    address_form = AddressForm(request.POST or None, instance=customer.address)
    customer_form = CustomerForm(request.POST or None, instance=customer)
    alarm_formset = alarm_formset_factory(request.POST or None, instance=customer)
    camera_formset = camera_formset_factory(request.POST or None, instance=customer)

    if request.method == "GET" or not forms_is_valid(
        address_form.is_valid(), customer_form.is_valid(), alarm_formset.is_valid(), camera_formset.is_valid()
    ):
        context = {
            "pg": "customers",
            "customer": customer,
            "address_form": address_form,
            "customer_form": customer_form,
            "alarm_formset": alarm_formset,
            "camera_formset": camera_formset,
        }
        return render(request, template_name, context)

    address_form.save()

    customer = customer_form.save()

    alarm_formset.instance = customer
    alarm_formset.save()

    camera_formset.instance = customer
    camera_formset.save()

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
