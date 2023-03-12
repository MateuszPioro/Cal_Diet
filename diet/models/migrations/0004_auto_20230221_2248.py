# Generated by Django 3.1.6 on 2023-02-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_auto_20230216_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='diary',
        ),
        migrations.AddField(
            model_name='diary',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='diary',
            name='products',
            field=models.ManyToManyField(to='models.Product'),
        ),
        migrations.DeleteModel(
            name='DiaryProduct',
        ),
    ]
