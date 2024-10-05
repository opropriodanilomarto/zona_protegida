"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Alarm(TimeStampedModel):
    customer = models.ForeignKey(
        "customers.Customer", verbose_name=_("customer"), on_delete=models.CASCADE, related_name="alarms"
    )
    description = models.CharField(_("Description"), max_length=255, blank=True)
    password_master = models.CharField(_("Password Master"), max_length=12, blank=True)
    mac = models.CharField(_("MAC"), max_length=32, blank=True)

    class Meta:
        ordering = ("description",)
        verbose_name = _("Alarm")
        verbose_name_plural = _("Alarms")

    def __str__(self) -> str:
        return str(self.description)


class Camera(TimeStampedModel):
    customer = models.ForeignKey(
        "customers.Customer", verbose_name=_("customer"), on_delete=models.CASCADE, related_name="cameras"
    )
    description = models.CharField(_("Description"), max_length=255, blank=True)
    serial = models.CharField(_("Serial"), max_length=255, blank=True)
    username = models.CharField(_("Username"), max_length=255, blank=True)
    password = models.CharField(_("Password"), max_length=255, blank=True)
    ip_adress = models.CharField(_("IP Address"), max_length=255, blank=True)

    class Meta:
        ordering = ("description",)
        verbose_name = _("camera")
        verbose_name_plural = _("cameras")

    def __str__(self) -> str:
        return str(
            f"'description': {self.description}, 'serial': {self.serial}, 'username': {self.username}, "
            f"'password': {self.password}, 'ip_adress': {self.ip_adress}"
        )
