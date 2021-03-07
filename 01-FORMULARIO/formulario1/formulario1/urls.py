"""formulario1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from form1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.index, name="inicio"),
    path('', views.index, name="index"),
    path('formulario/', views.formulario, name="formulario"),
    path('contacto/', views.contacto, name="contacto"),
    path('crear-usuario/<str:nombres>/<str:apellidos>/<str:documento>/<str:fechanacimiento>/<str:email>/<str:telefono>/<str:usuario>/<str:contraseña>/', views.crear_usuario, name="crear_usuario"),
    path('usuario/', views.usuario, name="usuario"),
    path('editar-usuario/<int:id>', views.editar_usuario),
    path('usuarios/', views.usuarios, name="usuarios"),
    path('borrar-usuario/<int:id>', views.borrar_usuario, name = "borrar"),
    path('create-full-usuario/', views.create_full_usuario, name="create_full")

]
