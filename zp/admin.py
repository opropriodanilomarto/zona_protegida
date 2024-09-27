from django.contrib import admin
from .models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "street",
        "number",
        "complement",
        "neighborhood",
        "city",
        "state",
        "country",
        "zip_code",
    )
