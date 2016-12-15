# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sede', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'sedes',
            },
        ),
    ]
