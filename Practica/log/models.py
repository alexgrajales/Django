from __future__ import unicode_literals
from django.db import models


class Log(models.Model):
    fecha = models.DateTimeField(auto_now=True)
    descripcion = models.TextField()

    class Meta:
        db_table = "log"
