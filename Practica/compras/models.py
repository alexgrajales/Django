from __future__ import unicode_literals
from django.db import models
from clientes.models import Cliente
from sedes.models import Sede
from productos.models import Producto


class Compra(models.Model):
    id_cliente = models.ForeignKey(Cliente, db_column='id_cliente')
    id_producto = models.ForeignKey(Producto, db_column='id_producto')
    id_sede = models.ForeignKey(Sede, db_column='id_sede')
    precio = models.PositiveIntegerField(default=0, blank=True, null=True)
    description = models.TextField()
    fecha = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "compras"

