# Generated by Django 4.0.1 on 2022-01-20 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='display',
            field=models.BooleanField(default=True, verbose_name='Display'),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='color',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='size',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.AddField(
            model_name='detailimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
