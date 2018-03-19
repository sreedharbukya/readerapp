# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-12 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(db_index=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.BigAutoField(db_index=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True, verbose_name=b'username')),
                ('first_name', models.CharField(max_length=60, verbose_name=b'First Name')),
                ('last_name', models.CharField(max_length=60, verbose_name=b'Last Name')),
                ('email', models.EmailField(blank=True, max_length=60, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'Reader',
            },
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together=set([('first_name', 'last_name')]),
        ),
    ]