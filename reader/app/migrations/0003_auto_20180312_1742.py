# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-12 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(blank=True, to='app.Author', verbose_name=b'Authors'),
        ),
    ]