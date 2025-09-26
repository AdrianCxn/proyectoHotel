from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('restaurante/', views.restaurante, name='restaurante')
]