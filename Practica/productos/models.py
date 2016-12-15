# coding=utf8
# -*- coding:utf8 -*-
from __future__ import unicode_literals
from django.db import models


class Producto(models.Model):
    producto = models.CharField(max_length=40)
    precio = models.PositiveIntegerField(default=0, blank=True, null=True)
    descripcion = models.TextField()

    class Meta:
        db_table = "productos"
