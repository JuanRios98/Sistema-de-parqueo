import rest_framework.serializers as clienteSerializer
from .models import Cliente

class clienteSerializer(clienteSerializer.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'