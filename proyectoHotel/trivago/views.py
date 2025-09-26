from django.http import HttpResponse
from django.shortcuts import render

from .models import Tipos

# Create your views here.
# Vista para index
def index(request):
    tipos = Tipos.objects.all()
    return render(request, "trivago/index.html")


# Vistas para habitaciones
def tipohabitacion(request):
    return render(request, "trivago/tipohabitacion.html")


def habitaciones(request):
    return render(request, "trivago/habitaciones.html")


# Vistas para administracion
def staff(request):
    return render(request, "trivago/staff.html")


def descuentos(request):
    return render(request, "trivago/descuentos.html")


def huespedes(request):
    return render(request, "trivago/huespedes.html")


def reservas(request):
    return render(request, "trivago/reservas.html")


def consumos(request):
    return render(request, "trivago/consumos.html")


# Vista para restaurante
def restaurante(request):
    return render(request, "trivago/restaurante.html")


# Vistas para productos
def productos(request):
    return render(request, "trivago/productos.html")


def inventario(request):
    return render(request, "trivago/inventario.html")


def distribuidores(request):
    return render(request, "trivago/distribuidores.html")