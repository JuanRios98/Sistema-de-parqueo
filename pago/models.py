from django.db import models
from parqueo.models import Parqueo
from cliente.models import Cliente

# Create your models here.
class Pago(models.Model):
    parqueo = models.ForeignKey(Parqueo, on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago {self.id} - {self.monto} {self.cliente if self.cliente else 'Sin Cliente'}"