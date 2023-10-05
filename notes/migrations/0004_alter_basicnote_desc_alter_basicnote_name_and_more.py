# Generated by Django 4.2.3 on 2023-09-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_basicnote_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicnote',
            name='desc',
            field=models.CharField(max_length=50, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='basicnote',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='basicnote',
            name='until',
            field=models.DateTimeField(verbose_name='Date'),
        ),
    ]
