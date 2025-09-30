from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Habitaciones, Tipos

# Create your views here.
# Vista para index
def index(request):
    tipos = Tipos.objects.all()
    return render(request, "trivago/index.html")

# Vistas para habitaciones
def tipohabitacion(request):
    return render(request, "trivago/tipohabitacion.html")

def habitaciones(request):
    habitaciones = Habitaciones.objects.all()
    return render(request, "trivago/habitaciones.html", {
        "habitaciones": habitaciones
    })

def agregar_habitacion(request):
    tipos = Tipos.objects.all()
    
    if request.method == "POST":
        numero = request.POST.get("numero")
        piso = request.POST.get("piso")
        id_tipo = request.POST.get("id_tipo")
        ocupado = request.POST.get("ocupado", 0)

        try:
            tipo = Tipos.objects.get(id_tipo=id_tipo)  # usar id_tipo
            nueva_habitacion = Habitaciones(
                numero=numero,
                piso=piso,
                id_tipo=tipo,
                ocupado=ocupado
            )
            nueva_habitacion.save()
            messages.success(request, "Habitación agregada exitosamente.")
            return redirect('habitaciones')
        except Tipos.DoesNotExist:
            messages.error(request, "El tipo de habitación no existe.")
        except IntegrityError:
            messages.error(request, "Error: El número de habitación ya existe.")
        except Exception as e:
            messages.error(request, f"Error al agregar la habitación: {e}")

    return render(request, "trivago/agregar_habitacion.html", {'tipos': tipos})


def editar_habitacion(request, id):
    habitacion = get_object_or_404(Habitaciones, pk=id)
    tipos = Tipos.objects.all()

    if request.method == "POST":
        habitacion.numero = request.POST.get('numero')
        habitacion.piso = request.POST.get('piso')
        id_tipo = request.POST.get('id_tipo')
        ocupado = request.POST.get('ocupado')

        try:
            habitacion.id_tipo = Tipos.objects.get(pk=id_tipo)
            habitacion.ocupado = True if ocupado == "1" else False
            habitacion.save()
            messages.success(request, "Habitación actualizada exitosamente.")

        except IntegrityError:
            messages.error(request, "Error: El número de habitación ya existe.")
        except Exception as e:
            messages.error(request, f"Error al actualizar la habitación: {e}")

    return render(request, "trivago/editar_habitacion.html", {
        "habitacion": habitacion,
        "tipos": tipos
    })


def eliminar_habitacion(request, id):
    habitacion = get_object_or_404(Habitaciones, pk=id)

    if request.method == "POST":
        try:
            habitacion.delete()
            messages.success(request, "Habitación eliminada exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al eliminar la habitación: {e}")
        return redirect("habitaciones")
    else:
        return redirect("habitaciones")


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