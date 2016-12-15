from django.shortcuts import render
from sedes.models import Sede


def createsede(request):
    return render(request, "Createsede.html", {'titulo': "Crear_sede"}, )


def readsede(request):
    try:
        list_sedes = Sede.objects.all()
        return render(request, "Readsede.html", {'titulo': "leer sede", 'sede': list_sedes}, )
    except Log.DoesNotExist:
        return render(request, "Readsede.html", {'titulo': "leer sede", 'sede': {}}, )
    except Exception:
        raise Exception.args


def editsede(request):
    return render(request, "Editsede.html", {'titulo': "editar_sede"}, )


def deletesede(request):
    return render(request, "Editsede.html", {'titulo': "editar_sede"}, )

