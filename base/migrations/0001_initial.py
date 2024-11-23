# Generated by Django 5.1 on 2024-09-02 01:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="customers",
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
                ("custId", models.IntegerField()),
                ("name", models.TextField(max_length=50)),
                ("password", models.TextField(max_length=50)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
