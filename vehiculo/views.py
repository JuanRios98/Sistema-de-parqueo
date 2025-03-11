from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Vehiculo
from .serializers import VehiculoSerializers

class VehiculoList(APIView):

    def get (self, request):
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializers(vehiculos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehiculoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehiculoDetail(APIView):

    def get(self, request, pk):
        vehiculos = get_object_or_404(Vehiculo, pk=pk)
        serializer = VehiculoSerializers(vehiculos)
        return Response(serializer.data)
    
    def put(self, request, pk):
        vehiculos = get_object_or_404(Vehiculo, pk=pk)
        serializer = VehiculoSerializers(vehiculos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        vehiculo = get_object_or_404(Vehiculo, pk=pk)
        vehiculo.delete()
        return Response({"message":"Vehiculo eliminado"},status=status.HTTP_204_NO_CONTENT)

    
# Create your views here.
