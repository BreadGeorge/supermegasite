# Generated by Django 4.2.3 on 2023-09-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_alter_basicnote_desc_alter_basicnote_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicnote',
            name='checkmark',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='basicnote',
            name='color',
            field=models.CharField(default='#fff700', max_length=7),
        ),
    ]