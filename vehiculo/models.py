from django.db import models
from cliente.models import Cliente
# Create your models here.
class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    placa = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'vehiculo'

    def __str__(self):
        return self.placa