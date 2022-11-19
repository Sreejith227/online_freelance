# Generated by Django 4.1.2 on 2022-11-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FeedbackModel",
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
                ("status", models.BooleanField(default=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=64)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=120)),
                ("message", models.TextField(max_length=500)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]