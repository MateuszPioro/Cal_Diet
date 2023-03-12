# Generated by Django 3.1.6 on 2023-02-16 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20230216_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='journals',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.RenameModel(
            old_name='Journal',
            new_name='Diary',
        ),
        migrations.DeleteModel(
            name='JournalProduct',
        ),
        migrations.AddField(
            model_name='diaryproduct',
            name='diar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.diary'),
        ),
        migrations.AddField(
            model_name='diaryproduct',
            name='produtct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='diary',
            field=models.ManyToManyField(through='models.DiaryProduct', to='models.Diary'),
        ),
    ]