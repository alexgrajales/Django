from __future__ import unicode_literals
from django.db import models


class Sede(models.Model):
    sede = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)

    class Meta:
        db_table = "sedes"
