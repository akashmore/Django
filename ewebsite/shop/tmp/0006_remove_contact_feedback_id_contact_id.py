# Generated by Django 4.2.1 on 2023-06-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0005_alter_contact_feedback_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="feedback_id",
        ),
        migrations.AddField(
            model_name="contact",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=0,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
    ]
