from django.db import models
from django.utils import timezone

class Zuñiga_Persona(models.Model):
    SEXO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    ]

    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    fecha_de_registro = models.DateTimeField(default=timezone.now)
