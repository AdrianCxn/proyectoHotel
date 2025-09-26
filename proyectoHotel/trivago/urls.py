from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Paths para habitaciones
    path('tipohabitacion/', views.tipohabitacion, name='tipohabitacion'),
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    # Paths para administracion
    path('staff/', views.staff, name='staff'),
    path('descuentos/', views.descuentos, name='descuentos'),
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