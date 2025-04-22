from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import Cliente
from .serializers import clienteSerializer
from django.views.generic import ListView



class ClienteList(APIView):
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = clienteSerializer(clientes, many=True)
        return render(request, 'cliente.html', {'clientes': clientes})
    
    def post(self, request):
        serializer = clienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Agrega más información sobre los errores
            return Response({
                'error': 'Los datos no son válidos',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
class ClienteDetail(APIView):

    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        clienteSerial = clienteSerializer(cliente)
        return Response(clienteSerial.data)

    def put(self, request ,pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        clienteSerial = clienteSerializer(cliente, data = request.data)
        if clienteSerial.is_valid():
            clienteSerial.save()
            return Response(clienteSerial.data, status = status.HTTP_200_OK)
        return Response(clienteSerial.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
            
    def delete (self,request,pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        cliente.delete()
        return Response({"message": "Cliente eliminado"},status=status.HTTP_204_NO_CONTENT)
        

    def listacliente(request):
        clientes = Cliente.objects.all()
        return render(request, 'cliente/cliente.html', {'clientes': clientes})
# Create your views here.
