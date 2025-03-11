import rest_framework.serializers as serializers
from .models import Celda

class CeldaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celda
        fields = '__all__'

