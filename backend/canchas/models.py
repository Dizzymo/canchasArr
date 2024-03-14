from django.db import models

class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_hora = models.DecimalField(max_digits=8, decimal_places=2)
    # Agrega más campos según tus necesidades

    def __str__(self):
        return self.nombre