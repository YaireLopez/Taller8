from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')


def formulario(request):
    return render(request, 'formulario.html')

def contacto(request):
    return render(request, 'contacto.html')