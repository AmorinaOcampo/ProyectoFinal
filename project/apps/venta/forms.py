from django import forms

from .models import Venta


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ["vendedor", "categoria", "servicio"]
        widgets = {
            "vendedor": forms.Select(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-control"}),
            "servicio": forms.Select(attrs={"class": "form-control"}),
        }
