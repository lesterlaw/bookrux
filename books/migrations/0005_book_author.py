# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-24 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20160322_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
