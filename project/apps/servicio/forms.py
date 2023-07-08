from django import forms

from .models import Servicio, ServicioCategoria


class ServicioCategoriaForm(forms.ModelForm):
    class Meta:
        model = ServicioCategoria
        fields = "__all__"

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"
