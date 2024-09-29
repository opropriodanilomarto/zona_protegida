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


class PersonQuerySet(models.QuerySet):
    pass


class PersonManager(models.Manager):
    pass


class Person(TimeStampedModel):
    class TypeService(models.TextChoices):
        ALARMS = "0", _("Only Alarms")
        CAMERAS = "1", _("Only Cameras")
        ALARMS_AND_CAMERAS = "2", _("Alarms and Cameras")

    employee = models.ForeignKey("auth.User", verbose_name=_("Employee"), on_delete=models.PROTECT)
    name = models.CharField(_("Name"), max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    type_service = models.CharField(
        _("Type of Service"), max_length=1, choices=TypeService, default=TypeService.ALARMS_AND_CAMERAS
    )
    address = models.ForeignKey("zp.Address", verbose_name=_("Adress"), on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(_("Deleted"), default=False)
    note = models.TextField(_("Note"), blank=True)
    objects = PersonManager.from_queryset(PersonQuerySet)

    class Meta:
        ordering = ("name",)
        verbose_name = _("Person")
        verbose_name_plural = _("People")
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self) -> str:
        return str(self.name)

    def save(self, *args, **kwargs) -> Self:
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("zp:customers:detail", kwargs={"slug": self.slug})

    def get_absolute_url_to_update(self) -> str:
        return reverse("zp:customers:update", kwargs={"slug": self.slug})

    def get_absolute_url_to_delete(self) -> str:
        return reverse("zp:customers:delete", kwargs={"slug": self.slug})
