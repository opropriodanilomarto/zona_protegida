"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from typing import Self

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from model_utils.models import TimeStampedModel
from django.utils.text import slugify


class CustomerQuerySet(models.QuerySet):
    pass


class CustomerManager(models.Manager):
    pass


class Customer(TimeStampedModel):
    class ServiceChoices(models.TextChoices):
        ALARMS = "alarms", _("Only Alarms")
        CAMERAS = "cameras", _("Only Cameras")
        ALARMS_AND_CAMERAS = "alarms_and_cameras", _("Alarms and Cameras")

    employee = models.ForeignKey("auth.User", verbose_name=_("Employee"), on_delete=models.PROTECT)
    name = models.CharField(_("Name"), max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    service_type = models.CharField(
        _("Service Type"), max_length=18, choices=ServiceChoices, default=ServiceChoices.ALARMS_AND_CAMERAS
    )
    address = models.ForeignKey(
        "zp.Address",
        verbose_name=_("Address"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="address",
    )
    deleted = models.BooleanField(_("Deleted"), default=False)
    note = models.TextField(_("Note"), blank=True)
    objects = CustomerManager.from_queryset(CustomerQuerySet)

    class Meta:
        ordering = ("name",)
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs) -> Self:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("zp:customers:customer_detail", kwargs={"slug": self.slug})

    def get_absolute_url_to_update(self) -> str:
        return reverse("zp:customers:customer_update", kwargs={"slug": self.slug})

    def get_absolute_url_to_delete(self) -> str:
        return reverse("zp:customers:customer_delete", kwargs={"slug": self.slug})
