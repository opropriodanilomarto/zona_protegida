"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "service_type", "employee")
    prepopulated_fields = {"slug": ["name"]}
    list_filter = ("service_type",)
