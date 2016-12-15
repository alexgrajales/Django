from django.shortcuts import render
from clientes.models  import Cliente


def createcliente(request):
    return render(request, "CreateCliente.html", {'titulo': "Crear Cliente"}, )

def readcliente(request):
    try:
        list_cliente = Cliente.objects.all()
        return render(request, "Readcliente.html", {'titulo': "leer cliente", 'cliente': list_cliente}, )
    except Log.DoesNotExist:
        return render(request, "Readcliente.html", {'titulo': "leer cliente", 'cliente': {}}, )
    except Exception:
        raise Exception.args

def editcliente(request):
    return render(request, "EditCliente.html", {'titulo': "editar Cliente"}, )


def deletecliente(request):
    return render(request, "EditCliente.html", {'titulo': "editar Cliente"}, )
