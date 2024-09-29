# Generated by Django 5.1.1 on 2024-09-27 07:47

import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("street", models.CharField(blank=True, max_length=255, verbose_name="Street")),
                ("number", models.CharField(blank=True, max_length=10, verbose_name="Number")),
                ("complement", models.CharField(blank=True, max_length=255, verbose_name="Complement")),
                ("neighborhood", models.CharField(blank=True, max_length=255, verbose_name="Neighborhood")),
                ("city", models.CharField(blank=True, max_length=255, verbose_name="City")),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("AC", "Acre"),
                            ("AL", "Alagoas"),
                            ("AP", "Amapá"),
                            ("AM", "Amazonas"),
                            ("BA", "Bahia"),
                            ("CE", "Ceará"),
                            ("DF", "Distrito Federal"),
                            ("ES", "Espírito Santo"),
                            ("GO", "Goiás"),
                            ("MA", "Maranhão"),
                            ("MT", "Mato Grosso"),
                            ("MS", "Mato Grosso do Sul"),
                            ("MG", "Minas Gerais"),
                            ("PA", "Pará"),
                            ("PB", "Paraíba"),
                            ("PR", "Paraná"),
                            ("PE", "Pernambuco"),
                            ("PI", "Piauí"),
                            ("RJ", "Rio de Janeiro"),
                            ("RN", "Rio Grande do Norte"),
                            ("RS", "Rio Grande do Sul"),
                            ("RO", "Rondônia"),
                            ("RR", "Roraima"),
                            ("SC", "Santa Catarina"),
                            ("SP", "São Paulo"),
                            ("SE", "Sergipe"),
                            ("TO", "Tocantins"),
                        ],
                        default="SP",
                        max_length=2,
                        verbose_name="State",
                    ),
                ),
                ("country", models.CharField(default="Brazil", max_length=255, verbose_name="Country")),
                ("zip_code", models.CharField(blank=True, max_length=10, verbose_name="Zip Code")),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
                "ordering": ("country", "state", "city", "neighborhood", "number", "street"),
            },
        ),
    ]
