# Generated by Django 4.1.9 on 2023-06-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=20)),
            ],
        ),
    ]