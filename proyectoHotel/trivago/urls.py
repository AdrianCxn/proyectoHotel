from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Paths para habitaciones
    path('tipohabitacion/', views.tipohabitacion, name='tipohabitacion'),
    path('editar_tipo_habitacion/<int:id>/', views.editar_tipohabitacion, name='editar_tipo_habitacion'),

    path('habitaciones/', views.habitaciones, name='habitaciones'),
    path('agregar_habitacion/', views.agregar_habitacion, name='agregar_habitacion'),
    path('editar_habitacion/<int:id>/', views.editar_habitacion, name='editar_habitacion'),
    path('eliminar_habitacion/<int:id>/', views.eliminar_habitacion, name='eliminar_habitacion'),

    # Paths para administracion
    path('staff/', views.staff, name='staff'),
    path('agregar_staff/', views.agregar_staff, name='agregar_staff'),
    path('editar_staff/<int:id>/', views.editar_staff, name='editar_staff'),
    path('eliminar_staff/<int:id>/', views.eliminar_staff, name='eliminar_staff'),

    path('descuentos/', views.descuentos, name='descuentos'),
    path('descuentos/agregar/', views.agregar_descuento, name='agregar_descuento'),
    path('descuentos/editar/<int:id>/', views.editar_descuento, name='editar_descuento'),
    path('descuentos/eliminar/<int:id>/', views.eliminar_descuento, name='eliminar_descuento'),

    path('huespedes/', views.huespedes, name='huespedes'),
    path('reservas/', views.reservas, name='reservas'),
    path('consumos/', views.consumos, name='consumos'),

    # Path para restaurante
    path('restaurante/', views.restaurante, name='restaurante'),

    # Paths para productos
    path('productos/', views.productos, name='productos'),
    path('inventario/', views.inventario, name='inventario'),
    path('distribuidores/', views.distribuidores, name='distribuidores')
]