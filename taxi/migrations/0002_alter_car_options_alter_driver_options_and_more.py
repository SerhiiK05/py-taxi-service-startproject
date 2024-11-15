# Generated by Django 5.1.3 on 2024-11-15 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="car",
            options={"ordering": ("model",), "verbose_name_plural": "cars"},
        ),
        migrations.AlterModelOptions(
            name="driver",
            options={"verbose_name_plural": "drivers"},
        ),
        migrations.AlterModelOptions(
            name="manufacturer",
            options={
                "ordering": ("name", "country"),
                "verbose_name_plural": "manufacturers",
            },
        ),
    ]
