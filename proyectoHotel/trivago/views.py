from django.http import HttpResponse
from django.shortcuts import render

from .models import Tipos

# Create your views here.
def main(request):
    tipos = Tipos.objects.all()
    return render(request, "trivago/index.html")


def restaurante(request):
    return render(request, "trivago/restaurante.html")


def tipohabitacion(request):
    return render(request, "trivago/tipohabitacion.html")