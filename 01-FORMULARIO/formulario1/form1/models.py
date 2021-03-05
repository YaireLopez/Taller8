from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.CharField(max_length=10)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    documento = models.CharField(max_length=15)
    fechanacimiento =  models.DateField
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=15)
    usuario = models.CharField(max_length=15)
    contraseña = models.

class TipoDocumento(models.Model):
    id= models.
    nombre= models.
    descripcion= models.

class Ciudad(models.Model):
    id= models.
    nombre= models.
    descripcion= models.