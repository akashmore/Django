# Generated by Django 4.2.1 on 2023-06-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="amount",
            field=models.IntegerField(default=0),
        ),
    ]