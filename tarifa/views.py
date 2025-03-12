from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Tarifa
from .serializers import TarifaSerializers

class TarifaList(APIView):
    def get(self,request):
        tarifa = Tarifa.objects.all()
        serializer = TarifaSerializers(tarifa, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TarifaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TarifaDetail(APIView):

    def get(self, request, pk):
        tarifa = get_object_or_404(Tarifa, pk=pk)
        serializer = TarifaSerializers(tarifa)
        return Response(serializer.data)
    
    def put(self, request, pk):
        tarifa = get_object_or_404(Tarifa, pk=pk)
        serializer = TarifaSerializers(tarifa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        tarifa = get_object_or_404(Tarifa, pk=pk)
        tarifa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
