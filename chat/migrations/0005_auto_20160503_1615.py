# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 08:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20160503_1615'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chat',
            unique_together=set([]),
        ),
    ]