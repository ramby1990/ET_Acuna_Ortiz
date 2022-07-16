from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from pet.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields =['rut', 'nombre', 'email', 'comuna', 'region', 'contraseña', 'telefono']