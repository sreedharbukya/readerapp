# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-12 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.BigAutoField(db_index=True, primary_key=True, serialize=False)),
                ('isbn_number', models.CharField(max_length=13, unique=True, verbose_name=b'ISBN Number')),
                ('title', models.CharField(max_length=100, verbose_name=b'Book Title')),
                ('author', models.ManyToManyField(blank=True, null=True, to='app.Author', verbose_name=b'Authors')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Reader', verbose_name=b'Book created by')),
            ],
            options={
                'verbose_name': 'Book',
            },
        ),
    ]
