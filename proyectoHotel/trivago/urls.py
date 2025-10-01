from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Paths para tipo de habitacion
    path('tipohabitacion/', views.tipohabitacion, name='tipohabitacion'),
    path('editar_tipo_habitacion/<int:id>/', views.editar_tipohabitacion, name='editar_tipo_habitacion'),

    # Paths para habitacion
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    path('agregar_habitacion/', views.agregar_habitacion, name='agregar_habitacion'),
    path('editar_habitacion/<int:id>/', views.editar_habitacion, name='editar_habitacion'),
    path('eliminar_habitacion/<int:id>/', views.eliminar_habitacion, name='eliminar_habitacion'),

    # Paths para staff
    path('staff/', views.staff, name='staff'),
    path('agregar_staff/', views.agregar_staff, name='agregar_staff'),
    path('editar_staff/<int:id>/', views.editar_staff, name='editar_staff'),
    path('eliminar_staff/<int:id>/', views.eliminar_staff, name='eliminar_staff'),

    # Paths para descuentos
    path('descuentos/', views.descuentos, name='descuentos'),
    path('agregar_descuento/', views.agregar_descuento, name='agregar_descuento'),
    path('editar_descuento/<int:id>/', views.editar_descuento, name='editar_descuento'),
    path('eliminar_descuento/<int:id>/', views.eliminar_descuento, name='eliminar_descuento'),

    # Paths para productos
    path('productos/', views.productos, name='productos'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    
    # Paths para inventario
    path('inventario/', views.inventario, name='inventario'),
    path('agregar_inventario/', views.agregar_inventario, name='agregar_inventario'),
    path('editar_inventario/<int:id>/', views.editar_inventario, name='editar_inventario'),
    path('eliminar_inventario/<int:id>/', views.eliminar_inventario, name='eliminar_inventario'),

    # Paths para distribuidor
    path('distribuidores/', views.distribuidores, name='distribuidores'),
    path('agregar_distribuidor/', views.agregar_distribuidor, name='agregar_distribuidor'),
    path('editar_distribuidor/<int:id>/', views.editar_distribuidor, name='editar_distribuidor'),
    path('eliminar_distribuidor/<int:id>/', views.eliminar_distribuidor, name='eliminar_distribuidor'),

    # Paths para huepedes
    path('huespedes/', views.huespedes, name='huespedes'),
    path('eliminar_huesped/<int:id>/', views.eliminar_huesped, name='eliminar_huesped'),

    # Paths para reservas
    path('reservas/', views.reservas, name='reservas'),
    path('editar_reserva/<int:id>/', views.editar_reserva, name='editar_reserva'),
    path('eliminar_reserva/<int:id>/', views.eliminar_reserva, name='eliminar_reserva'),

    path('consumos/', views.consumos, name='consumos'),

    # Path para restaurante
    path('restaurante/', views.restaurante, name='restaurante'),
]