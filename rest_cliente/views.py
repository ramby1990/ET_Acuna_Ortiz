
from urllib import request, response
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from .serializers import ClienteSerializer
from  pet.models import Cliente
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_clientes(request):
    if request.method == 'GET':
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


