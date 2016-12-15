"""Practica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# coding=utf8
# -*- coding:utf8 -*-


from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from home.views import index
from productos.views import createproducto
from productos.views import deleteproducto
from productos.views import editproducto
from productos.views import readproducto
from sedes.views import createsede
from sedes.views import deletesede
from sedes.views import editsede
from sedes.views import readsede

from compras.views import createcompra
from compras.views import deletecompra
from compras.views import editcompra
from compras.views import readcompra

from clientes.views import createcliente
from clientes.views import deletecliente
from clientes.views import editcliente
from clientes.views import readcliente


from log.views import createlog
from log.views import deletelog
from log.views import editlog
from log.views import readlog

urlpatterns = [
    # url(r'^', TemplateView.as_view(template_name='index.html'), name='index'), se direcciona
    url(r'^$', index, name="home"),
    url(r'^createproducto/$', createproducto, name="crear_producto"),
    url(r'^$', deleteproducto, name="borrar producto"),
    url(r'^$', editproducto, name="editar producto"),
    url(r'^readproducto/$', readproducto, name="leer_producto"),

    url(r'^createsede/$', createsede, name="sede"),
    url(r'^$', deletesede, name="borrar sede"),
    url(r'^$', editsede, name="editar sede"),
    url(r'^readsede/$', readsede, name="leer_sede"),


    url(r'^createcliente/$', createcliente, name="cliente"),
    url(r'^$', deletecliente, name="borrar cliente"),
    url(r'^$', editcliente, name="editar cliente"),
    url(r'^readcliente/$', readcliente, name="leer_cliente"),

    url(r'^createcliente/$', createcompra, name="compra"),
    url(r'^$', deletecompra, name="borrar compra"),
    url(r'^$', editcompra, name="editar compra"),
    url(r'^readcliente/$', readcompra, name="leer_compra"),

    url(r'^createlog/$', createlog, name="crear log"),
    url(r'^$', deletelog, name="borrar log"),
    url(r'^$', editlog, name="editar log"),
    url(r'^readlog/$', readlog, name="leer_log"),

    # url(r'^product/(?P<pk>)/$', readproducto.productodetalle),

    # url(r'^createproducto/createproducto.css', TemplateView.as_view(template_name='createProducto.css'), name='crear_produtos'),

    url(r'^admin/', admin.site.urls),
]
