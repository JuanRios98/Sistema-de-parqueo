from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response    
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Celda
from .serializers import CeldaSerializer
from rest_framework import status

# Create your views here.

def home (request):
    return HttpResponse("Hola Mundo")


class CeldaList(APIView):

    def get(self, request):
        celdas = Celda.objects.all()
        serializer = CeldaSerializer(celdas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CeldaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        celda = get_object_or_404(Celda, pk=pk)
        serializer = CeldaSerializer(celda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    
    def delete(self, request):
        celdas = Celda.objects.all()
        celdas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


