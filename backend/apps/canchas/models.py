from django.db import models
from model_utils.models import TimeStampedModel



class Cancha(TimeStampedModel):
    nombre = models.CharField('Nombre',max_length=100)
    descripcion = models.TextField()
    precio_hora = models.DecimalField(max_digits=8, decimal_places=2)
    # Agrega más campos según tus necesidades

    def __str__(self):
        return self.nombre