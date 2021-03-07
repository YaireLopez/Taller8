from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    documento = models.CharField(max_length=20)
    fechanacimiento = models.DateTimeField
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=15)
    usuario = models.CharField(max_length=15)

class TipoDocumento(models.Model):
    nombre= models.CharField(max_length=30)
    descripcion= models.TextField(max_length=300)

class Ciudad(models.Model):
    nombre= models.CharField(max_length=30)
    descripcion= models.TextField(max_length=300)