from distutils.command.upload import upload
import email
from pickle import TRUE
from pyexpat import model
from urllib import request
from django.db import models
from django.forms import CharField

# Create your models here.

class Accesorio(models.Model):
    id =models.CharField(primary_key=True,max_length=6)
    nombre = models.CharField(max_length=64)
    descripcion =models.TextField(null=True)
    precio = models.PositiveSmallIntegerField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'



class Cliente(models.Model):
    rut=models.CharField(primary_key=True,max_length=12)
    nombre=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    comuna=models.IntegerField(
        
        
    )
    region=models.IntegerField(
        null=False, blank=False,
        
        
    )
    contraseña=models.CharField(max_length=50)
    telefono=models.IntegerField(null=True, blank=True)

    def __str__(self):
        
        return self.rut