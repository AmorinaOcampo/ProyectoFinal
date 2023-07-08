from django.contrib import admin

from . import models

admin.site.register(models.Vendedor)


@admin.register(models.Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = (
        "vendedor",
        "servicio",
        "precio_total",
        "fecha_venta",
    )
    list_display_links = ("servicio",)
    search_fields = ("servicio.nombre", "vendedor")
    list_filter = ("vendedor",)
    date_hierarchy = "fecha_venta"
