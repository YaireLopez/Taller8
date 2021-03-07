
from django.shortcuts import render, HttpResponse, redirect
from form1.models import Usuario, Ciudad, TipoDocumento
from form1.forms import formUsuario

# Create your views here.
def index(request):
    return render(request, 'index.html')


def formulario(request):
    return render(request, 'formulario.html')

def contacto(request):
    return render(request, 'contacto.html')

def crear_usuario(request,nombres,apellidos,documento,fechanacimiento,email,telefono,usuario):
    usuario= Usuario(
        nombres = nombres,
        apellidos = apellidos,
        documento =  documento,
        fechanacimiento = fechanacimiento,
        email = email,
        telefono = telefono,
        usuario = usuario,
    )
    usuario.save()

    return HttpResponse(f"Usuario creado: {usuario.nombres} - {usuario.apellidos} - {usuario.documento} - {usuario.fechanacimiento} - {usuario.email} - {usuario.telefono} - {usuario.usuario}")

def usuario(request):

    usuario = Usuario.objects.get()
    return HttpResponse(f"Usuario: <br/> {usuario.nombres}. {usuario.apellidos}. {usuario.documento}. {usuario.fechanacimiento}. {usuario.email}. {usuario.telefono}. {usuario.usuario}")

def editar_usuario(request, id):

    usuario = Usuario.objects.get(pk=id)

    nombres = "sofia"
    apellidos = "gomez"
    documento = "1293"
    fechanacimiento =  "02-02-2001"
    email = "sof@gmail.com"
    telefono = "949300"
    usuario = "sofju"

    usuario.save()


    return HttpResponse(f"Usuario editado: <br/> {usuario.nombres}. {usuario.apellidos}. {usuario.documento}. {usuario.fechanacimiento}. {usuario.email}. {usuario.telefono}. {usuario.usuario}")

def usuarios(request):
    usuarios = Usuario.objects.order_by('id')
    return render(request, 'usuarios.html', {
        'usuarios': usuarios
    })

def borrar_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()

    return redirect('usuarios')

def create_full_usuario(request):

    if request.method == 'POST':
        formulario = FormUsuario(request.POST)
        if formulario.is_valid():
            data_form =  formulario.cleaned_data

            
    else:
        
        formulario = formUsuario()

    return render(request, 'create_full_usuario.html', {
        'form': formulario
    })