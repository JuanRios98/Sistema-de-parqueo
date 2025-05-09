from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TipoPlan(models.TextChoices):
    MENSUAL = 'mensual', 'Mensualidad'
    OCASIONAL = 'ocasional', 'Ocasional'

class Cliente(models.Model):
    tipo_plan = models.CharField(max_length=10, choices=TipoPlan.choices)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    class Meta:
        db_table = 'cliente'

 