from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='portal_index'),
    path('registro/', views.registro, name='registro_huesped'),
    path('login/', views.login_huesped, name='login_huesped'),
    path('logout/', views.logout_huesped, name='logout_huesped'),
    path('dashboard/', views.huesped_dashboard, name='huesped_dashboard'),
    path('reserva/<int:id_reserva>/reporte/', views.reporte_reserva, name='reporte_reserva'),
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
]