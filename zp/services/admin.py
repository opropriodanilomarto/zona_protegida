from django.contrib import admin
from .models import Alarm, Camera


@admin.register(Alarm)
class AlarmAdmin(admin.ModelAdmin):
    list_display = ("description",)


@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ("description",)
