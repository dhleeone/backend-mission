# Generated by Django 4.0.1 on 2022-01-22 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_detailimage_product_display_product_sale_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='stock',
            field=models.PositiveIntegerField(null=True),
        ),
    ]