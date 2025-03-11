from rest_framework import serializers
from .models import Parqueo


class ParqueoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parqueo
        fields = '__all__'
