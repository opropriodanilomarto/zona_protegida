"""
Zona Protegida is an open source web application under the MIT license.

Contributions to this module:
    * Danilo Marto de Carvalho <carvalho.dm@proton.me>
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class Address(TimeStampedModel):
    class ChooseState(models.TextChoices):
        AC = "AC", _("Acre")
        AL = "AL", _("Alagoas")
        AP = "AP", _("Amapá")
        AM = "AM", _("Amazonas")
        BA = "BA", _("Bahia")
        CE = "CE", _("Ceará")
        DF = "DF", _("Distrito Federal")
        ES = "ES", _("Espírito Santo")
        GO = "GO", _("Goiás")
        MA = "MA", _("Maranhão")
        MT = "MT", _("Mato Grosso")
        MS = "MS", _("Mato Grosso do Sul")
        MG = "MG", _("Minas Gerais")
        PA = "PA", _("Pará")
        PB = "PB", _("Paraíba")
        PR = "PR", _("Paraná")
        PE = "PE", _("Pernambuco")
        PI = "PI", _("Piauí")
        RJ = "RJ", _("Rio de Janeiro")
        RN = "RN", _("Rio Grande do Norte")
        RS = "RS", _("Rio Grande do Sul")
        RO = "RO", _("Rondônia")
        RR = "RR", _("Roraima")
        SC = "SC", _("Santa Catarina")
        SP = "SP", _("São Paulo")
        SE = "SE", _("Sergipe")
        TO = "TO", _("Tocantins")

    street = models.CharField(_("Street"), max_length=255, blank=True)
    number = models.CharField(_("Number"), max_length=10, blank=True)
    complement = models.CharField(_("Complement"), max_length=255, blank=True)
    neighborhood = models.CharField(_("Neighborhood"), max_length=255, blank=True)
    city = models.CharField(_("City"), max_length=255, blank=True)
    state = models.CharField(_("State"), max_length=2, choices=ChooseState.choices, default=ChooseState.SP)
    country = models.CharField(_("Country"), max_length=255, default=_("Brazil"))
    zip_code = models.CharField(_("Zip Code"), max_length=10, blank=True)

    class Meta:
        ordering = ("country", "state", "city", "neighborhood", "number", "street")
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self) -> str:
        return str(
            f"{self.street}, {self.number}, {self.complement if self.complement else ""} "
            f"- {self.neighborhood}, {self.city} - {self.state}, {self.zip_code}"
        )
