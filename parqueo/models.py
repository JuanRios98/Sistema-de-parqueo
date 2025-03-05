from django.db import models
from vehiculo.models import Vehiculo
from celda.models import Celda  
from tarifa.models import Tarifa

# Create your models here.
class EstadoParqueo(models.TextChoices):
    ACTIVO = 'activo', 'Activo'
    FINALIZADO = 'finalizado', 'Finalizado'

class Parqueo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    celda = models.ForeignKey(Celda, on_delete=models.CASCADE)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.RESTRICT)
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estado = models.CharField(max_length=10, choices=EstadoParqueo.choices, default=EstadoParqueo.ACTIVO)

    def __str__(self):
        return f"Parqueo {self.id} - {self.vehiculo.placa} ({self.get_estado_display()})"