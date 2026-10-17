from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('recuperar/', views.recuperar_password, name='recuperar_password'),
    path('recuperar/validar/', views.validar_codigo, name='validar_codigo'),
    path('recuperar/nueva/', views.nueva_password, name='nueva_password'), # <-- Última ruta
]