# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 08:23
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.crypto
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('Fiction', 'Fiction'), ('Business', 'Business'), ('Adventure', 'Adventure')], max_length=100)),
                ('description', models.TextField()),
                ('personal_review', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(default=django.utils.crypto.get_random_string, max_length=13, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(blank=True, choices=[('Good', 'Good'), ('Neutral', 'Neutral'), ('Bad', 'Bad')], max_length=100, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('published_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=b'', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='user')),
                ('shelf', models.ManyToManyField(blank=True, null=True, to='books.Book')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
