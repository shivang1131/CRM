# Generated by Django 5.0.3 on 2024-03-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=15)),
                ("address", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("province", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
            ],
        ),
    ]
