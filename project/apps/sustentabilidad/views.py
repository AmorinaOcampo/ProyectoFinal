from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


class SustentabilidadDetail(DetailView):
    model = models.Sustentabilidad


class SustentabilidadList(ListView):
    model = models.Sustentabilidad

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Sustentabilidad.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Sustentabilidad.objects.all()
        return object_list


class SustentabilidadCreate(CreateView):
    model = models.Sustentabilidad
    form_class = forms.SustentabilidadForm
    success_url = reverse_lazy("sustentabilidad:index")


class SustentabilidadDelete(DeleteView):
    model = models.Sustentabilidad
    success_url = reverse_lazy("sustentabilidad:sustentabilidad_list")


class SustentabilidadUpdate(UpdateView):
    model = models.Sustentabilidad
    success_url = reverse_lazy("sustentabilidad:sustentabilidad_list")
    form_class = forms.SustentabilidadForm
