from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/', views.registrar_mascota, name='registrar_mascota'),
    path('mascota/<int:id>/', views.perfil_mascota, name='perfil_mascota'),
    path('registrada/<int:id>/', views.mascota_registrada, name='mascota_registrada'),
]

