from rest_framework import serializers
from .models import Vehiculo

class VehiculoSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Vehiculo
        fields = '__all__'