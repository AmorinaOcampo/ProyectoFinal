from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Sustentabilidad(models.Model):
    """Sustentabilidad"""

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")

    class Meta:
        verbose_name = "sustentabilidad"

    def __str__(self):
        """Representa una instancia de la clase como una cadena de texto."""
        return self.nombre



