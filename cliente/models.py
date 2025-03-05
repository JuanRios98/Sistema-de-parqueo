from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TipoPlan(models.TextChoices):
    MENSUAL = 'mensual', 'Mensualidad'
    OCASIONAL = 'ocasional', 'Ocasional'

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    tipo_plan = models.CharField(max_length=10, choices=TipoPlan.choices)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username