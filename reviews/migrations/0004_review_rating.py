# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 15:37
from __future__ import unicode_literals

from django.db import migrations
import likert_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=likert_field.models.LikertField(blank=True, null=True),
        ),
    ]
