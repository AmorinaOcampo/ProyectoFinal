from django import forms

from .models import Sustentabilidad


class SustentabilidadForm(forms.ModelForm):
    class Meta:
        model = Sustentabilidad
        fields = ["nombre", "descripcion"]
        widgets = {
            "nombre": forms.Select(attrs={"class": "form-control"}),
            "descripcion": forms.Select(attrs={"class": "form-control"}),
        }
