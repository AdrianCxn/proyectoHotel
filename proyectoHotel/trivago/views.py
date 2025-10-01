from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .models import Habitaciones, Huespedes, Reservas, Staffs, Tipos, Descuentos, Productos, Distribuidores, Inventarios

# Create your views here.
# Vista para index
def index(request):
    tipos = Tipos.objects.all()
    return render(request, "trivago/index.html")


# Vistas para tipo de habitaciones
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

# Vistas para habitaciones
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


# Vistas para staff
def staff(request):
    staff = Staffs.objects.all()
    return render(request, "trivago/staff/staff.html", {
        "staff": staff
    })

def agregar_staff(request):
    if request.method == "POST":
        # Campos obligatorios básicos
        nombre = request.POST.get("nombre") or ""
        pr_apellido = request.POST.get("pr_apellido") or ""
        telefono = request.POST.get("telefono") or ""
        email = request.POST.get("email") or ""
        edad = request.POST.get("edad") or ""
        salario = request.POST.get("salario") or ""

        # Campos opcionales: si vienen vacíos -> None
        se_apellido = (request.POST.get("se_apellido") or None) or None
        area_trabajo = (request.POST.get("area_trabajo") or None) or None
        turno = (request.POST.get("turno") or None) or None

        if not (nombre and pr_apellido and telefono and email and edad and salario):
            messages.error(request, "Faltan campos obligatorios.")
            return render(request, "trivago/staff/agregar_staff.html")

        try:
            nuevo_staff = Staffs(
                nombre=nombre,
                pr_apellido=pr_apellido,
                se_apellido=se_apellido,
                telefono=telefono,
                email=email,
                edad=edad,
                area_trabajo=area_trabajo,
                salario=salario,
                turno=turno
            )
            nuevo_staff.save()
            messages.success(request, "Staff agregado exitosamente.")
            return redirect('staff')
        except IntegrityError:
            messages.error(request, "Teléfono o email ya registrados.")
        except Exception as e:
            messages.error(request, f"Error al agregar el staff: {e}")

    return render(request, "trivago/staff/agregar_staff.html")

def editar_staff(request, id):
    staff = get_object_or_404(Staffs, pk=id)

    if request.method == "POST":
        staff.nombre = request.POST.get("nombre")
        staff.pr_apellido = request.POST.get("pr_apellido")
        staff.se_apellido = request.POST.get("se_apellido")
        staff.telefono = request.POST.get("telefono")
        staff.email = request.POST.get("email")
        staff.edad = request.POST.get("edad")
        staff.area_trabajo = request.POST.get("area_trabajo")
        staff.salario = request.POST.get("salario")
        staff.turno = request.POST.get("turno")

        try:
            staff.save()
            messages.success(request, "Staff actualizado exitosamente.")
            return redirect('staff')
        except IntegrityError:
            messages.error(request, "Error: Ya existe un staff con estos datos.")
        except Exception as e:
            messages.error(request, f"Error al actualizar el staff: {e}")

    return render(request, "trivago/staff/editar_staff.html", {
        "staff": staff
    })

def eliminar_staff(request, id):
    staff = get_object_or_404(Staffs, pk=id)

    if request.method == "POST":
        try:
            staff.delete()
            messages.success(request, "Staff eliminado exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al eliminar el staff: {e}")
        return redirect("staff")
    else:
        return redirect("staff")

# Vistas para descuentos
def descuentos(request):
    descuentos = Descuentos.objects.all()
    return render(request, "trivago/descuentos/descuentos.html", {
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

    return render(request, "trivago/descuentos/agregar_descuento.html")

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

    return render(request, "trivago/descuentos/editar_descuento.html", {
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
    productos = Productos.objects.all()
    return render(request, "trivago/productos/productos.html", {
        "productos": productos
    })

def agregar_producto(request):
    productos = Productos.objects.all()
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        marca = request.POST.get("marca")
        costo = request.POST.get("costo")

        try:
            nuevo_producto = Productos(
                nombre=nombre,
                marca=marca,
                costo=costo
            )
            nuevo_producto.save()
            messages.success(request, "Producto agregado exitosamente.")
            return redirect('productos') 
        except IntegrityError:
            messages.error(request, "Error: Ya existe ese producto.")
        except Exception as e:
            messages.error(request, f"Error al agregar nuevo producto: {e}")

    return render(request, "trivago/productos/agregar_producto.html")

def editar_producto(request, id):
    producto = get_object_or_404(Productos, pk=id)

    if request.method == "POST":
        producto.nombre = request.POST.get('nombre')
        producto.marca = request.POST.get('marca')
        producto.costo = request.POST.get('costo')

        try:
            producto.save()
            messages.success(request, "Producto actualizado exitosamente.")
            return redirect('productos')  # redirige a la lista de descuentos
        except IntegrityError:
            messages.error(request, "Error: Ya existe un producto con estos datos.")
        except Exception as e:
            messages.error(request, f"Error al actualizar el producto: {e}")

    return render(request, "trivago/productos/editar_producto.html", {
        "producto": producto
    })

def eliminar_producto(request, id):
    productos = get_object_or_404(Productos, pk=id)

    if request.method == "POST":
        try:
            productos.delete()
            messages.success(request, "Producto eliminado exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al eliminar el producto: {e}")
        return redirect("productos")
    else:
        return redirect("productos")


# Vistas para distribuidores
def distribuidores(request):
    distribuidores = Distribuidores.objects.all()
    return render(request, "trivago/distribuidores/distribuidores.html", {
        "distribuidores": distribuidores
    })

def agregar_distribuidor(request):
    distribuidores = Distribuidores.objects.all()
    if request.method == "POST": 
        marca = request.POST.get("marca")
        telefono = request.POST.get("telefono")
        email = request.POST.get("email")
        try:
            nuevo_distribuidor = Distribuidores(
                marca=marca,
                telefono=telefono,
                email=email
            )
            nuevo_distribuidor.save()
            messages.success(request, "Distribuidor agregado exitosamente.")
            return redirect('distribuidores') 
        except IntegrityError:
            messages.error(request, "Error: Ya existe ese distribuidor.")
        except Exception as e:
            messages.error(request, f"Error al agregar nuevo distribuidor: {e}")

    return render(request, "trivago/distribuidores/agregar_distribuidor.html")

def editar_distribuidor(request, id):
    distribuidor = get_object_or_404(Distribuidores, pk=id)

    if request.method == "POST":
        distribuidor.telefono = request.POST.get('telefono')
        distribuidor.email = request.POST.get('email')

        try:
            distribuidor.save()
            messages.success(request, "Distribuidor actualizado exitosamente.")
            return redirect('distribuidores') 
        except IntegrityError:
            messages.error(request, "Error: Ya existe un distribuidor con estos datos.")
        except Exception as e:
            messages.error(request, f"Error al actualizar el distribuidor: {e}")

    return render(request, "trivago/distribuidores/editar_distribuidor.html", {
        "distribuidor": distribuidor
    })  

def eliminar_distribuidor(request, id):
    distribuidores = get_object_or_404(Distribuidores, pk=id)

    if request.method == "POST":
        try:
            distribuidores.delete()
            messages.success(request, "Distribuidor eliminado exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al eliminar el distribuidor: {e}")
        return redirect("distribuidores")
    else:
        return redirect("distribuidores")
    
# Vistas para inventarios
def inventario(request):
    inventarios = Inventarios.objects.all()
    return render(request, "trivago/inventarios/inventario.html", {
        "inventarios": inventarios
    })

def agregar_inventario(request):
    productos_usados = Inventarios.objects.values_list("id_producto", flat=True)
    productos = Productos.objects.exclude(id_producto__in=productos_usados)
    distribuidores = Distribuidores.objects.all()
    
    if request.method == "POST":
        id_producto = request.POST.get("id_producto")
        id_distribuidor = request.POST.get("id_distribuidor")
        cantidad = request.POST.get("cantidad")

        try:
            productos = Productos.objects.get(id_producto=id_producto)
            distribuidores = Distribuidores.objects.get(id_distribuidor=id_distribuidor)  
            nuevo_inventario = Inventarios(
                id_producto=productos,
                id_distribuidor=distribuidores,
                cantidad=cantidad,
            )
            nuevo_inventario.save()
            messages.success(request, "Nuevo registro agregado al inventario exitosamente.")
            return redirect('inventario')
        except Productos.DoesNotExist:
            messages.error(request, "El producto no existe.")
        except Distribuidores.DoesNotExist:
            messages.error(request, "El distribuidor no existe.")
        except IntegrityError:
            messages.error(request, "Error: El registro ya existe.")
        except Exception as e:
            messages.error(request, f"Error al agregar el registro: {e}")
    return render(request, "trivago/inventarios/agregar_inventario.html", {
        "inventario": inventario,
        "distribuidores": distribuidores,
        "productos": productos
    })
   
from .models import Inventarios, Productos, Distribuidores

def editar_inventario(request, id):
    inventario = get_object_or_404(Inventarios, pk=id)
    distribuidores = Distribuidores.objects.all()

    if request.method == "POST":
        id_distribuidor = request.POST.get("id_distribuidor")
        cantidad = request.POST.get("cantidad")

        inventario.id_distribuidor = Distribuidores.objects.get(pk=id_distribuidor)
        inventario.cantidad = cantidad
        inventario.save()
        messages.success(request, "Inventario actualizado exitosamente.")
        return redirect("inventario")

    return render(request, "trivago/inventarios/editar_inventario.html", {
        "inventario": inventario,
        "productos": productos,
        "distribuidores": distribuidores,
    })


def eliminar_inventario(request, id):
    inventario = get_object_or_404(Inventarios, pk=id)

    if request.method == "POST":
        try:
            inventario.delete()
            messages.success(request, "Registro eliminado exitosamente.")
        except Exception as e:
            messages.error(request, f"Error al eliminar el registro: {e}")
        return redirect('inventario')
    else:
        return redirect("inventario")