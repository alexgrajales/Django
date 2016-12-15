from __future__ import unicode_literals
from django.db import models


class Cliente(models.Model):
    documento = models.PositiveIntegerField(default=0, blank=True, null=True)
    nombres = models.CharField(max_length=80)
    detalles = models.TextField()

    class Meta:
        db_table = "clientes"
