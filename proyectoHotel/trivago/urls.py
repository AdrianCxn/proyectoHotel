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

    path('descuentos/', views.descuentos, name='descuentos'),
    path('agregar_descuento/', views.agregar_descuento, name='agregar_descuento'),
    path('editar_descuento/<int:id>/', views.editar_descuento, name='editar_descuento'),
    path('eliminar_descuento/<int:id>/', views.eliminar_descuento, name='eliminar_descuento'),

    path('huespedes/', views.huespedes, name='huespedes'),
    path('reservas/', views.reservas, name='reservas'),
    path('consumos/', views.consumos, name='consumos'),

    # Path para restaurante
    path('restaurante/', views.restaurante, name='restaurante'),

    # Paths para productos
    path('productos/', views.productos, name='productos'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    



    path('inventario/', views.inventario, name='inventario'),
    path('distribuidores/', views.distribuidores, name='distribuidores')
]