# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20160210_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='book',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='book',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]