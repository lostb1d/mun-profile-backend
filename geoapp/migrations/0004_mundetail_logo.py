# Generated by Django 4.2.7 on 2023-11-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0003_occupation_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='mundetail',
            name='logo',
            field=models.ImageField(default='', null='TRUE', upload_to='images/'),
            preserve_default='TRUE',
        ),
    ]
