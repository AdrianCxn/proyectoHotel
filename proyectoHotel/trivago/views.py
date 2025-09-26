from django.http import HttpResponse
from django.shortcuts import render

from .models import Tipos

# Create your views here.
def main(request):
    tipos = Tipos.objects.all()
    return render(request, "trivago/main.html", {
        'tipos': tipos
    })


def ejemplo(request):
    return render(request, "trivago/ejemplo.html")