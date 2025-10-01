from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Habitaciones, Huespedes, Reservas, Staffs, Tipos

# Create your views here.
# Vista para index
def index(request):
    tipos = Tipos.objects.all()
    return render(request, "trivago/index.html")


# Vistas para habitaciones
def tipohabitacion(request):
    tipos = Tipos.objects.all()
    return render(request, "trivago/tipohabitacion/tipohabitacion.html", {
        "tipos": tipos
    })


def editar_tipohabitacion(request, id):
    tipo = get_object_or_404(Tipos, pk=id)
    
    if request.method == "POST":
        precio = request.POST.get("precio")

        try:
            tipo.precio = precio
            tipo.save()
            messages.success(request, "Tipo de habitación actualizado exitosamente.")
            return redirect('tipohabitacion')
        except Exception as e:
            messages.error(request, f"Error al actualizar el tipo de habitación: {e}")
    return render(request, "trivago/tipohabitacion/editar_tipo_habitacion.html", {
        "tipo": tipo
    })


def habitaciones(request):
    habitaciones = Habitaciones.objects.all()
    return render(request, "trivago/habitaciones/habitaciones.html", {
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

    return render(request, "trivago/habitaciones/agregar_habitacion.html", {'tipos': tipos})


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
            return redirect('habitaciones')
        except IntegrityError:
            messages.error(request, "Error: El número de habitación ya existe.")
        except Exception as e:
            messages.error(request, f"Error al actualizar la habitación: {e}")

    return render(request, "trivago/habitaciones/editar_habitacion.html", {
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
    staff = Staffs.objects.all()
    return render(request, "trivago/staff/staff.html", {
        "staff": staff
    })


def agregar_staff(request):
    return render(request, "trivago/staff/gregar_staff.html")


def editar_staff(request, id):
    return render(request, "trivago/staff/editar_staff.html")


def eliminar_staff(request, id):
    pass

def descuentos(request):
    descuentos = Descuentos.objects.all()
    return render(request, "trivago/descuentos.html", {
        "descuentos": descuentos
    })

def agregar_descuento(request):
    descuentos = Descuentos.objects.all()
    if request.method == "POST":
        fecha_inicio = request.POST.get("fecha_inicio")
        fecha_fin = request.POST.get("fecha_fin")
        porcentaje = request.POST.get("descuento")

        try:
            nuevo_descuento = Descuentos(
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin,
                descuento=porcentaje
            )
            nuevo_descuento.save()
            messages.success(request, "Descuento agregado exitosamente.")
            return redirect('descuentos') 
        except IntegrityError:
            messages.error(request, "Error: Ya existe un descuento con estos datos.")
        except Exception as e:
            messages.error(request, f"Error al agregar el descuento: {e}")

    return render(request, "trivago/agregar_descuento.html")

def editar_descuento(request, id):
    descuento = get_object_or_404(Descuentos, pk=id)

    if request.method == "POST":
        descuento.fecha_inicio = request.POST.get('fecha_inicio')
        descuento.fecha_fin = request.POST.get('fecha_fin')
        descuento.descuento = request.POST.get('descuento')

        try:
            descuento.save()
            messages.success(request, "Descuento actualizado exitosamente.")
            return redirect('descuentos')  # redirige a la lista de descuentos
        except IntegrityError:
            messages.error(request, "Error: Ya existe un descuento con estos datos.")
        except Exception as e:
            messages.error(request, f"Error al actualizar el descuento: {e}")

    return render(request, "trivago/editar_descuento.html", {
        "descuento": descuento
    })

def eliminar_descuento(request, id):
    descuentos = get_object_or_404(Descuentos, pk=id)

    if request.method == "POST":
        try:
            descuentos.delete()
            messages.success(request, "Descuento eliminado exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al eliminar el descuento: {e}")
        return redirect("descuentos")
    else:
        return redirect("descuentos")
    



def huespedes(request):
    huespedes = Huespedes.objects.all()
    return render(request, "trivago/huespedes.html", {
        "huespedes": huespedes
    })


def reservas(request):
    reservas = Reservas.objects.all()
    return render(request, "trivago/reservas.html", {
        "reservas": reservas
    })


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