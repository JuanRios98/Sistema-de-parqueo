from django.db import models

# Create your models here.
class TipoCelda(models.TextChoices):
    AUTOMOVIL = 'automovil', 'Automóvil'
    MOTO = 'moto', 'Moto'

class EstadoCelda(models.TextChoices):
    LIBRE = 'libre', 'Libre'
    OCUPADO = 'ocupado', 'Ocupado'
    RESERVADO = 'reservado', 'Reservado'

class Celda(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=10, choices=TipoCelda.choices)
    estado = models.CharField(max_length=10, choices=EstadoCelda.choices, default=EstadoCelda.LIBRE)

    def __str__(self):
        return f"Celda {self.codigo} ({self.get_tipo_display()})"
