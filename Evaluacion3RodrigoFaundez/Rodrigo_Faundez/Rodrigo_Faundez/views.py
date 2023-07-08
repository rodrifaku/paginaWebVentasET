from django.shortcuts import render

from m_venta.models import Producto
from .productos import productos


def mostrar_principal(request):
    return render(request, 'principal.html')


def mostrar_productos(request):
    contexto = {
        'productos': Producto.objects.all()
    }
    return render(request, 'productos.html', contexto)
