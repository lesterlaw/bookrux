# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 05:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20160208_0327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='book',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='book',
            name='image4',
        ),
    ]
