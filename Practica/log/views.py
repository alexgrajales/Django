from django.shortcuts import render
from log.models import Log


def createlog(request):
    return render(request, "Createlog.html", {'titulo': "Crear_log"}, )


def readlog(request):
    try:
        list_log = Log.objects.all()
        return render(request, "Readlog.html", {'titulo': "leer log", 'log': list_log}, )
    except Log.DoesNotExist:
        return render(request, "Readlog.html", {'titulo': "leer log", 'log': {}}, )
    except Exception:
        raise Exception.args


def editlog(request):
    return render(request, "Editlog.html", {'titulo': "editar_log"}, )


def deletelog(request):
    return render(request, "Editlog.html", {'titulo': "editar_log"}, )