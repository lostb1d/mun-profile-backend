# Generated by Django 4.2.7 on 2023-11-20 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warddetail',
            old_name='no',
            new_name='wardNo',
        ),
    ]