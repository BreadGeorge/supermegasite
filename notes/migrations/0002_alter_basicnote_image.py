# Generated by Django 4.2.3 on 2023-09-26 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicnote',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
