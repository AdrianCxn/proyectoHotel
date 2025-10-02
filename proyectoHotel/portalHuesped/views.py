from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from trivago.models import Productos, Rerestaurantes, Reservas, Huespedes, Cuentas, Consumos, Habitaciones, Tipos, Descuentos
from .models import HuespedCuenta


def index(request):
    if request.user.is_authenticated:
        return redirect('huesped_dashboard')
    return render(request, 'portalHuesped/index.html')


def registro(request):
    #Registro de huésped sin reserva. Se crea usuario y registro en huespedes con ID_RESERVA en NULL.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        nombre = request.POST.get('nombre')
        pr_apellido = request.POST.get('pr_apellido')
        se_apellido = request.POST.get('se_apellido') or None
        telefono = request.POST.get('telefono')
        edad = request.POST.get('edad')

        if not all([username, password, email, nombre, pr_apellido, telefono, edad]):
            messages.error(request, 'Todos los campos obligatorios deben llenarse.')
            return redirect('registro_huesped')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('registro_huesped')
        if Huespedes.objects.filter(email=email).exists():
            messages.error(request, 'Ya existe un huésped con ese email.')
            return redirect('registro_huesped')
        if Huespedes.objects.filter(telefono=telefono).exists():
            messages.error(request, 'Ese telefono ya esta registrado.')
            return redirect('registro_huesped')

        
        huesped = Huespedes.objects.create(
            nombre=nombre,
            pr_apellido=pr_apellido,
            se_apellido=se_apellido,
            telefono=telefono,
            email=email,
            edad=edad,
        )

        # Eto e' para crear el usuario con nombre y apellido porque no se guarda automaticamente
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=nombre,         # Primer nombre
            last_name=pr_apellido      # Primer apellido
        )
        HuespedCuenta.objects.create(user=user, huesped=huesped)
        messages.success(request, 'Cuenta creada correctamente. Ahora puedes iniciar sesión.')
        return redirect('login_huesped')

    return render(request, 'portalHuesped/registro.html')


def login_huesped(request):
    if request.user.is_authenticated:
        return redirect('huesped_dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Validar que tenga cuenta de huésped
            try:
                user.huesped_cuenta
            except HuespedCuenta.DoesNotExist:
                messages.error(request, 'Tu usuario no está vinculado a un huésped.')
                return redirect('login_huesped')
            login(request, user)
            return redirect('huesped_dashboard')
        else:
            messages.error(request, 'Credenciales inválidas.')
    return render(request, 'portalHuesped/login.html')


def logout_huesped(request):
    logout(request)
    return redirect('login_huesped')


@login_required
def huesped_dashboard(request):
    try:
        cuenta = request.user.huesped_cuenta
    except Exception:
        # Si el usuario no tiene cuenta de huésped, cerrar sesión y redirigir al login
        logout(request)
        messages.error(request, "Tu cuenta ha sido eliminada. Inicia sesión nuevamente o contacta al administrador.")
        return redirect('login_huesped')
    reservas = Reservas.objects.filter(id_huesped=cuenta.huesped.id_huesped).distinct()
    reservas_restaurante = Rerestaurantes.objects.filter(id_huesped=cuenta.huesped.id_huesped)
    sin_reserva = not reservas.exists()
    return render(request, 'portalHuesped/dashboard.html', {
        'cuenta': cuenta,
        'reservas': reservas,
        'sin_reserva': sin_reserva,
        'reservas_restaurante': reservas_restaurante,
    })


@login_required
def reporte_reserva(request, id_reserva: int):
    cuenta = request.user.huesped_cuenta
    reserva = get_object_or_404(Reservas, pk=id_reserva, id_huesped=cuenta.huesped.id_huesped)
    # Datos financieros y consumos
    cuenta_reserva = Cuentas.objects.filter(id_reserva=reserva).first()
    consumos = Consumos.objects.filter(id_reserva=reserva).select_related('id_producto')
    total_consumos = 0
    for c in consumos:
        if hasattr(c.id_producto, 'costo') and c.cantidad:
            total_consumos += c.id_producto.costo * c.cantidad

    return render(request, 'portalHuesped/reporte_reserva.html', {
        'reserva': reserva,
        'cuenta_reserva': cuenta_reserva,
        'consumos': consumos,
        'total_consumos': total_consumos,
    })


@login_required
def crear_reserva(request):
    """Permite al huésped crear una reserva si hay habitaciones disponibles.

    Reglas:
    - Seleccionar fechas y tipo de habitación.
    - Filtrar habitaciones libres en el rango.
    - Validar capacidad (adultos + niños).
    - Asignar descuento opcional si existe id descuento válido.
    """
    cuenta = request.user.huesped_cuenta

    from django.utils.dateparse import parse_datetime
    tipos = Tipos.objects.all()
    descuentos = Descuentos.objects.all()

    fecha_llegada = request.POST.get('fecha_llegada') if request.method == 'POST' else None
    fecha_salida = request.POST.get('fecha_salida') if request.method == 'POST' else None

    # Filtrar descuentos si ya hay fechas seleccionadas
    descuentos_filtrados = descuentos
    fl = fs = None
    if fecha_llegada and fecha_salida:
        fl = parse_datetime(fecha_llegada.replace('T', ' '))
        fs = parse_datetime(fecha_salida.replace('T', ' '))
        if fl and fs:
            descuentos_filtrados = descuentos.filter(fecha_inicio__lte=fl.date(), fecha_fin__gte=fs.date())

    if request.method == 'POST':
        adultos = request.POST.get('adultos')
        ninos = request.POST.get('ninos')
        id_tipo = request.POST.get('id_tipo')
        id_descuento = request.POST.get('id_descuento')
        metodo_pago = request.POST.get('metodo_pago')

        if not all([fecha_llegada, fecha_salida, adultos, ninos, id_tipo, metodo_pago]):
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('crear_reserva')
        if not fl or not fs:
            messages.error(request, 'Formato de fecha inválido.')
            return redirect('crear_reserva')
        if fs <= fl:
            messages.error(request, 'La fecha de salida debe ser posterior a la de llegada.')
            return redirect('crear_reserva')

        adultos_i = int(adultos)
        ninos_i = int(ninos)
        total_personas = adultos_i + ninos_i

        reservas_conflictivas = Reservas.objects.filter(
            id_habitacion__id_tipo__id_tipo=id_tipo,
            activa=1,
            fecha_llegada__lt=fs,
            fecha_salida__gt=fl
        ).values_list('id_habitacion_id', flat=True)

        habitaciones_disponibles = Habitaciones.objects.filter(id_tipo__id_tipo=id_tipo).exclude(id_habitacion__in=reservas_conflictivas)

        if not habitaciones_disponibles.exists():
            messages.error(request, 'No hay habitaciones disponibles para ese rango de fechas y tipo.')
            return redirect('crear_reserva')

        habitacion = habitaciones_disponibles.first()
        tipo = habitacion.id_tipo
        if tipo.tipo == 'Sencilla' and total_personas > 1:
            messages.error(request, 'Capacidad excedida para habitación Sencilla (máx 1).')
            return redirect('crear_reserva')
        if tipo.tipo == 'Duplex' and total_personas > 2:
            messages.error(request, 'Capacidad excedida para habitación Duplex (máx 2).')
            return redirect('crear_reserva')
        if tipo.tipo == 'Familiar' and total_personas > 4:
            messages.error(request, 'Capacidad excedida para habitación Familiar (máx 4).')
            return redirect('crear_reserva')
        if tipo.tipo == 'Suit' and total_personas > 6:
            messages.error(request, 'Capacidad excedida para habitación Suit (máx 6).')
            return redirect('crear_reserva')

        descuento_obj = None
        if id_descuento:
            try:
                descuento_obj = descuentos_filtrados.get(id_descuento=id_descuento)
            except Descuentos.DoesNotExist:
                messages.warning(request, 'Descuento no válido o no aplica a las fechas seleccionadas, se ignora.')

        noches = (fs - fl).days

        try:
            reserva = Reservas.objects.create(
                id_huesped=cuenta.huesped,
                id_habitacion=habitacion,
                fecha_llegada=fl,
                fecha_salida=fs,
                cantidad_a=adultos_i,
                cantidad_n=ninos_i,
                capacidad_total=total_personas,
                metodo_pago=metodo_pago,
                activa=1,
                id_descuento=descuento_obj if descuento_obj else None
            )
            
            # Crear la cuenta aprovechando el trigger que calcula automáticamente noches y total
            cuenta_reserva = Cuentas.objects.create(
                id_reserva=reserva,
                # Los campos noches y total los calculará automáticamente el trigger
                noches=0,  # Valor temporal que será actualizado por el trigger
                total=0.00  # Valor temporal que será actualizado por el trigger
            )

            messages.success(request, f'Reserva creada exitosamente (# {reserva.id_reserva}). La cuenta se ha generado automáticamente.')
            return redirect('huesped_dashboard')
        except Exception as e:
            messages.error(request, f'Error al crear la reserva: {e}')
            return redirect('crear_reserva')

    return render(request, 'portalHuesped/crear_reserva.html', {
        'tipos': tipos,
        'descuentos': descuentos_filtrados,
    })


@login_required
def crear_reserva_restaurante(request):
    cuenta = request.user.huesped_cuenta
    
    # Generar fechas disponibles (hoy y los próximos 6 días)
    from datetime import date, timedelta
    fechas_disponibles = []
    for i in range(7):
        fecha = date.today() + timedelta(days=i)
        fechas_disponibles.append(fecha.strftime('%Y-%m-%d'))
    
    # Horas disponibles (de 8:00 a 17:00 cada hora)
    horas_disponibles = [
        "8:00", "9:00", "10:00", "11:00", "12:00",
        "13:00", "14:00", "15:00", "16:00", "17:00", 
    ]
    
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        personas = request.POST.get('numero_personas')

        # Validar que todos los campos estén completos
        if not all([fecha, hora, personas]):
            messages.error(request, 'Todos los campos son obligatorios.')
            return render(request, 'portalHuesped/crear_reserva_restaurante.html', {
                'fechas_disponibles': fechas_disponibles,
                'horas_disponibles': horas_disponibles,
            })

        # Validar que la fecha no sea anterior a hoy
        from datetime import datetime
        fecha_seleccionada = datetime.strptime(fecha, '%Y-%m-%d').date()
        if fecha_seleccionada < date.today():
            messages.error(request, 'No puedes reservar una fecha anterior a hoy.')
            return render(request, 'portalHuesped/crear_reserva_restaurante.html', {
                'fechas_disponibles': fechas_disponibles,
                'horas_disponibles': horas_disponibles,
            })

        try:
            # Crear la reserva de restaurante
            from trivago.models import Rerestaurantes
            reserva_restaurant = Rerestaurantes.objects.create(
                id_huesped=cuenta.huesped,
                personas=int(personas),
                fecha=fecha,
                hora=hora,
                activa=1
            )
            messages.success(request, f'Reserva de restaurante creada exitosamente para {personas} personas.')
            return redirect('huesped_dashboard')
        except Exception as e:
            messages.error(request, f'Error al crear la reserva de restaurante: {e}')

    return render(request, 'portalHuesped/crear_reserva_restaurante.html', {
        'fechas_disponibles': fechas_disponibles,
        'horas_disponibles': horas_disponibles,
    })


@login_required
def comprar(request):
    """Vista que solo muestra la lista de productos disponibles"""
    cuenta = request.user.huesped_cuenta
    from trivago.models import Productos
    productos = Productos.objects.all()
    reservas_activas = Reservas.objects.filter(id_huesped=cuenta.huesped, activa=1)

    return render(request, 'portalHuesped/comprar.html', {
        'cuenta': cuenta,
        'productos': productos,
        'reservas_activas': reservas_activas
    })


@login_required
def comprar_producto(request, producto_id):
    """Vista específica para procesar la compra de un producto específico"""
    cuenta = request.user.huesped_cuenta
    
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')
        reserva_id = request.POST.get('reserva_id')
        
        if not all([cantidad, reserva_id]):
            messages.error(request, 'La cantidad y la reserva son obligatorias.')
            return redirect('comprar')
            
        try:
            cantidad_i = int(cantidad)
            if cantidad_i <= 0:
                raise ValueError("La cantidad debe ser un número positivo.")
            
            from trivago.models import Productos, Consumos
            producto = Productos.objects.get(id_producto=producto_id)
            
            # Verificar que la reserva pertenece al huésped y está activa
            reserva = get_object_or_404(Reservas, id_reserva=reserva_id, id_huesped=cuenta.huesped, activa=1)
            
            Consumos.objects.create(
                id_reserva=reserva,
                id_producto=producto,
                cantidad=cantidad_i
            )
            
            messages.success(request, f'Se agregó {cantidad_i} unidades de {producto.nombre} a tu consumo.')
            
        except Productos.DoesNotExist:
            messages.error(request, 'El producto seleccionado no existe.')
        except ValueError as ve:
            messages.error(request, f'Error en la cantidad: {ve}')
        except Exception as e:
            messages.error(request, f'Error al procesar la compra: {e}')
    
    return redirect('comprar')
