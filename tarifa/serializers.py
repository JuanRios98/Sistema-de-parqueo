from rest_framework import serializers
from .models import Tarifa

class TarifaSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Tarifa
        fields = '__all__'