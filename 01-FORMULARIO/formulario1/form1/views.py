
from django.shortcuts import render, HttpResponse, redirect
from form1.models import Persona, Ciudad, TipoDocumento

# Create your views here.
def index(request):
    return render(request, 'index.html')


def formulario(request):
    return render(request, 'formulario.html')

def contacto(request):
    return render(request, 'contacto.html')

def crear_usuario(request):
    usuario= Usuario(
        nombres = "Nombres"
        apellidos = "Apellidos"
        documento =  "Número de documento"
        fechanacimiento = "Fecha de acimiento"
        email = "Email"
        telefono = "Teléfono"
        usuario = "usuario"
        contraseña = "contraseña"

    )

    return HttpResponse("Usuario creado: ")