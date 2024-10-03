# Generated by Django 5.1.1 on 2024-10-02 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0002_alter_customer_service_type"),
        ("zp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="address",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="address",
                to="zp.address",
                verbose_name="Address",
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="service_type",
            field=models.CharField(
                choices=[
                    ("alarms", "Only Alarms"),
                    ("cameras", "Only Cameras"),
                    ("alarms_and_cameras", "Alarms and Cameras"),
                ],
                default="alarms_and_cameras",
                max_length=18,
                verbose_name="Service Type",
            ),
        ),
    ]
