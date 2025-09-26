from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('ejemplo/', views.ejemplo, name='ejemplo')
]