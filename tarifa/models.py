from django.db import models
from celda.models import TipoCelda
# Create your models here.
class TipoTarifa(models.TextChoices):
    HORA = 'hora', 'Por Hora'
    MENSUAL = 'mensual', 'Mensual'

class Tarifa(models.Model):
    tipo = models.CharField(max_length=10, choices=TipoTarifa.choices)
    vehiculo_tipo = models.CharField(max_length=10, choices=TipoCelda.choices)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tarifa {self.get_tipo_display()} ({self.get_vehiculo_tipo_display()}) - {self.monto}"