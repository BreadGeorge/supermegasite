# Generated by Django 4.2.3 on 2023-10-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_alter_scheduleblock_endtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicnote',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]