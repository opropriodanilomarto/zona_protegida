"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "type_person", "type_service", "employee")
    search_fields = ("query",)
    prepopulated_fields = {"slug": ["name"]}
    list_filter = ("type_person", "type_service")
