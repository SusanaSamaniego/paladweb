from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('cita.html/', views.cita, name='cita.html'),
    path('CREAR.html/', views.CREAR, name='CREAR.html'),
    path('EDITAR.html/', views.EDITAR, name='EDITAR.html'),
    path('ELIMINAR.html/', views.ELIMINAR, name='ELIMINAR.html'),
    path('PV.html/', views.PV, name='PV.html'),
     path('login.html/', views.login, name='login.html'),
      path('logout.html/', views.logout, name='logout.html'),
  
  
]