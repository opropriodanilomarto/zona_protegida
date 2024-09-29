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
    class TypePerson(models.TextChoices):
        NP = "NP", _("Natural Person")
        LE = "LE", _("Legal Entity")

    class TypeService(models.TextChoices):
        OA = "OA", _("Only Alarms")
        OC = "OC", _("Only Cameras")
        AC = "AC", _("Alarms and Cameras")

    employee = models.ForeignKey("auth.User", verbose_name=_("Employee"), on_delete=models.PROTECT)
    name = models.CharField(_("Name"), max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    type_person = models.CharField(_("Type of Person"), max_length=2, choices=TypePerson.choices, default=TypePerson.NP)
    type_service = models.CharField(
        _("Type of Service"), max_length=2, choices=TypeService.choices, default=TypeService.AC
    )
    address = models.ForeignKey("zp.Address", verbose_name=_("Adress"), on_delete=models.SET_NULL, null=True)
    query = models.TextField(_("query"))
    deleted = models.BooleanField(_("Deleted"), default=False)
    note = models.TextField(_("Note"), blank=True)

    objects = PersonManager.from_queryset(PersonQuerySet)

    class Meta:
        ordering = ("name",)
        verbose_name = _("Person")
        verbose_name_plural = _("People")
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["query"]),
        ]

    def __str__(self) -> str:
        return str(self.name)

    def get_absolute_url(self) -> str:
        return reverse("zp:customers:detail", kwargs={"slug": self.slug})

    def get_absolute_url_to_update(self) -> str:
        return reverse("zp:customers:update", kwargs={"slug": self.slug})

    def get_absolute_url_to_delete(self) -> str:
        return reverse("zp:customers:delete", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs) -> Self:
        self.slug = slugify(self.name)
        self.query = f"{self.name} {self.type_person} {self.type_service} {self.address} {self.employee}"
        return super().save(*args, **kwargs)
