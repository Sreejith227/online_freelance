# Generated by Django 4.1.2 on 2022-11-21 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_freelancermodel_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="profilemodel",
            name="email_id",
            field=models.CharField(default="emailid", max_length=150),
        ),
    ]