# Generated by Django 4.1.7 on 2023-05-03 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprofile',
            name='image',
            field=models.ImageField(upload_to='profile_images'),
        ),
    ]
