# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_sede', to='clientes.Cliente'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='id_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_sede', to='productos.Producto'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='id_sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_sede', to='sedes.Sede'),
        ),
    ]
