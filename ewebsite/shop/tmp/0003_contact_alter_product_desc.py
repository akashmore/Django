# Generated by Django 4.2.1 on 2023-06-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_product_category_product_image_product_price_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="contact",
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
                ("name", models.CharField(max_length=100)),
                ("surname", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("subject", models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name="product",
            name="desc",
            field=models.CharField(max_length=1000),
        ),
    ]