# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 19:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('productos', '0002_auto_20161214_1415'),
        ('sedes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
                ('id_sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sedes.Sede')),
            ],
            options={
                'db_table': 'compras',
            },
        ),
    ]
