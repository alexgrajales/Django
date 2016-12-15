from django.shortcuts import render
from compras.models import Compra


def createcompra(request):
    return render(request, "Createcompra.html", {'titulo': "Crear_compra"}, )


def readcompra(request):
    try:
        list_compra = Compra.objects.all()
        return render(request, "Readcompra.html", {'titulo': "leer compra", 'compra': list_compra}, )
    except Log.DoesNotExist:
        return render(request, "Readcompra.html", {'titulo': "leer compra", 'compra': {}}, )
    except Exception:
        raise Exception.args


def editcompra(request):
    return render(request, "Editcompra.html", {'titulo': "editar_compra"}, )


def deletecompra(request):
    return render(request, "Editcompra.html", {'titulo': "editar_compra"}, )
