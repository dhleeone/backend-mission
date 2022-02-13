# Generated by Django 4.0.1 on 2022-01-12 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='market',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='shop.market'),
        ),
    ]
