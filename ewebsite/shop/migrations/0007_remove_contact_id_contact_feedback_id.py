# Generated by Django 4.2.1 on 2023-06-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0006_remove_contact_feedback_id_contact_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="id",
        ),
        migrations.AddField(
            model_name="contact",
            name="feedback_id",
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]