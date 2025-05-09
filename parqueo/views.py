from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Parqueo
from .serializers import ParqueoSerializers

class ParqueoList(APIView):

    def get(self, request):
        parqueo = Parqueo.objects.all()
        serializer = ParqueoSerializers(parqueo, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ParqueoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ParqueoDetail(APIView):

    def get(self, request, pk):
        parqueo = get_object_or_404(Parqueo, pk=pk)
        serializer = ParqueoSerializers(parqueo)
        return Response(serializer.data)
    

    def put(self, request, pk):
        parqueo = get_object_or_404(Parqueo, pk=pk)
        serializer = ParqueoSerializers(parqueo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        parqueo = get_object_or_404(Parqueo, pk=pk)
        parqueo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
