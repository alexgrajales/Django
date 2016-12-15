from django.shortcuts import render
from productos.models import Producto
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader


def readproducto(request):
    try:
        list_product = Producto.objects.all()
        return render(request, "ReadProducto.html", {'titulo': "leer Producto", 'products': list_product}, )
    except Producto.DoesNotExist:
        return render(request, "ReadProducto.html", {'titulo': "leer Producto", 'products': {}}, )
    except Exception:
        raise Exception.args


def createproducto(request):
    return render(request, "CreateProducto.html", {'titulo': "Crear Producto"}, )
        # template = loader.get_template('productodetalle.html')
        # form = ProductForm()
        # contex = {
        #     'product': product
        # }
        # return HttpResponse(template.render(contex, request))


def deleteproducto(request):
    return render(request, "DeleteProducto.html", {'titulo': "borrar Producto"}, )


def editproducto(request):
    return render(request, "EditProducto.html", {'titulo': "Editar Producto"}, )


def productodetalle(request, pk):
        product = get_object_or_404(Producto, pk=pk)
        template = loader.get_template('productodetalle.html')
        contex = {
            'product': product
        }
        return HttpResponse(template.render(contex, request))


