# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Consumos(models.Model):
    id_consumo = models.AutoField(db_column='ID_CONSUMO', primary_key=True)  # Field name made lowercase.
    id_reserva = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='ID_RESERVA')  # Field name made lowercase.
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='ID_PRODUCTO')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consumos'


class Cuentas(models.Model):
    id_cuenta = models.AutoField(db_column='ID_CUENTA', primary_key=True)  # Field name made lowercase.
    noches = models.IntegerField(db_column='NOCHES')  # Field name made lowercase.
    total = models.DecimalField(db_column='TOTAL', max_digits=14, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    id_reserva = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='ID_RESERVA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuentas'


class Distribuidores(models.Model):
    id_distribuidor = models.AutoField(db_column='ID_DISTRIBUIDOR', primary_key=True)  # Field name made lowercase.
    marca = models.CharField(db_column='MARCA', max_length=50)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', unique=True, max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'distribuidores'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Habitaciones(models.Model):
    id_habitacion = models.AutoField(db_column='ID_HABITACION', primary_key=True)  # Field name made lowercase.
    numero = models.IntegerField(db_column='NUMERO', unique=True)  # Field name made lowercase.
    piso = models.IntegerField(db_column='PISO')  # Field name made lowercase.
    id_tipo = models.ForeignKey('Tipos', models.DO_NOTHING, db_column='ID_TIPO')  # Field name made lowercase.
    ocupado = models.IntegerField(db_column='OCUPADO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'habitaciones'


class Huespedes(models.Model):
    id_huesped = models.AutoField(db_column='ID_HUESPED', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50)  # Field name made lowercase.
    pr_apellido = models.CharField(db_column='PR_APELLIDO', max_length=50)  # Field name made lowercase.
    se_apellido = models.CharField(db_column='SE_APELLIDO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', unique=True, max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', unique=True, max_length=50)  # Field name made lowercase.
    edad = models.IntegerField(db_column='EDAD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'huespedes'


class Inventarios(models.Model):
    id_inventario = models.AutoField(db_column='ID_INVENTARIO', primary_key=True)  # Field name made lowercase.
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='ID_PRODUCTO')  # Field name made lowercase.
    id_distribuidor = models.ForeignKey(Distribuidores, models.DO_NOTHING, db_column='ID_DISTRIBUIDOR')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='CANTIDAD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventarios'


class PortalhuespedHuespedcuenta(models.Model):
    id = models.BigAutoField(primary_key=True)
    creado = models.DateTimeField()
    actualizado = models.DateTimeField()
    huesped = models.OneToOneField(Huespedes, models.DO_NOTHING)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portalhuesped_huespedcuenta'


class Productos(models.Model):
    id_producto = models.AutoField(db_column='ID_PRODUCTO', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50)  # Field name made lowercase.
    marca = models.CharField(db_column='MARCA', max_length=50)  # Field name made lowercase.
    costo = models.DecimalField(db_column='COSTO', max_digits=7, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productos'


class Descuentos(models.Model):
    id_descuento = models.AutoField(db_column='ID_DESCUENTO', primary_key=True)
    fecha_inicio = models.DateField(db_column='FECHA_INICIO')
    fecha_fin = models.DateField(db_column='FECHA_FIN')
    descuento = models.DecimalField(db_column='DESCUENTO', max_digits=8, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'descuentos'


class Reservas(models.Model):
    id_reserva = models.AutoField(db_column='ID_RESERVA', primary_key=True)  # Field name made lowercase.
    id_habitacion = models.ForeignKey(Habitaciones, models.DO_NOTHING, db_column='ID_HABITACION')  # Field name made lowercase.
    fecha_llegada = models.DateTimeField(db_column='FECHA_LLEGADA')  # Field name made lowercase.
    fecha_salida = models.DateTimeField(db_column='FECHA_SALIDA')  # Field name made lowercase.
    capacidad_total = models.IntegerField(db_column='CAPACIDAD_TOTAL')  # Field name made lowercase.
    cantidad_a = models.IntegerField(db_column='CANTIDAD_A')  # Field name made lowercase.
    cantidad_n = models.IntegerField(db_column='CANTIDAD_N')  # Field name made lowercase.
    metodo_pago = models.CharField(db_column='METODO_PAGO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    activa = models.IntegerField(db_column='ACTIVA')  # Field name made lowercase.
    id_descuento = models.ForeignKey(Descuentos, models.DO_NOTHING, db_column='ID_DESCUENTO', blank=True, null=True)  # Field name made lowercase.
    id_huesped = models.ForeignKey(Huespedes, models.DO_NOTHING, db_column='ID_HUESPED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservas'

class Rerestaurantes(models.Model):
    id_restaurant = models.AutoField(db_column='ID_RESTAURANT', primary_key=True)  # Field name made lowercase.
    id_huesped = models.ForeignKey(Huespedes, models.DO_NOTHING, db_column='ID_HUESPED')  # Field name made lowercase.
    personas = models.IntegerField(db_column='PERSONAS')  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA')
    hora = models.TimeField(db_column='HORA')   # Field name made lowercase.
    activa = models.IntegerField(db_column='ACTIVA')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'rerestaurantes'


class Restaurant(models.Model):
    id_rest = models.AutoField(db_column='ID_REST', primary_key=True)  # Field name made lowercase.
    id_staff = models.ForeignKey('Staffs', models.DO_NOTHING, db_column='ID_STAFF', null=True, blank=True)  # Field name made lowercase.
    id_restaurant = models.ForeignKey(Rerestaurantes, models.DO_NOTHING, db_column='ID_RESTAURANT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'restaurant'


class Staffs(models.Model):
    id_staff = models.AutoField(db_column='ID_STAFF', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50)  # Field name made lowercase.
    pr_apellido = models.CharField(db_column='PR_APELLIDO', max_length=50)  # Field name made lowercase.
    se_apellido = models.CharField(db_column='SE_APELLIDO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', unique=True, max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', unique=True, max_length=50)  # Field name made lowercase.
    edad = models.IntegerField(db_column='EDAD')  # Field name made lowercase.
    area_trabajo = models.CharField(db_column='AREA_TRABAJO', max_length=19, blank=True, null=True)  # Field name made lowercase.
    salario = models.DecimalField(db_column='SALARIO', max_digits=8, decimal_places=2)  # Field name made lowercase.
    turno = models.CharField(db_column='TURNO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staffs'


class Tipos(models.Model):
    id_tipo = models.AutoField(db_column='ID_TIPO', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cama = models.IntegerField(db_column='CAMA')  # Field name made lowercase.
    baños = models.IntegerField(db_column='BAÑOS')  # Field name made lowercase.
    capacidad_total = models.IntegerField(db_column='CAPACIDAD_TOTAL')  # Field name made lowercase.
    capacidad_a = models.IntegerField(db_column='CAPACIDAD_A')  # Field name made lowercase.
    capacidad_n = models.IntegerField(db_column='CAPACIDAD_N')  # Field name made lowercase.
    cocineta = models.IntegerField(db_column='COCINETA')  # Field name made lowercase.
    televisor = models.IntegerField(db_column='TELEVISOR')  # Field name made lowercase.
    vista = models.CharField(db_column='VISTA', max_length=7, blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='PRECIO', max_digits=8, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipos'
