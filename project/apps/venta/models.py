from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendedor")
    celular = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatars", blank=True, null=True)

    class Meta:
        verbose_name = "vendedor"
        verbose_name_plural = "vendedores"

    def __str__(self):
        return f"{self.usuario.username}"


class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey("servicio.serviciocategoria", on_delete=models.DO_NOTHING)
    servicio = models.ForeignKey("servicio.servicio", on_delete=models.DO_NOTHING)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        ordering = ("-fecha_venta",)

    def save(self, *args, **kwargs):
        self.precio_total = self.servicio.precio + 500
        super().save(*args, **kwargs)