from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse


def index(request):
    # return HttpResponseRedirect('http://stackoverflow.com/questions/22892651/how-to-default-integerfield-in-django')
    # return  HttpResponse('index.html')//contexto
    # return render(request, "index.html", {'hola': "Alex"}, )//le envio desde la vista algo al template
    return render(request, "index.html", {'titulo': "Producto"}, )


