# Generated by Django 3.1.6 on 2023-03-01 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_product_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
    ]
