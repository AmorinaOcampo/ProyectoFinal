from django.contrib import admin

from . import models

admin.site.site_title = "sustentabilidad"
admin.site.site_header = "IntLOGIC"


@admin.register(models.Sustentabilidad)
class SustentabilidadAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "descripcion",
    )
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)