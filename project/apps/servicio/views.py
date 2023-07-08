from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

# **** Categoría de Servicios


class ServicioCategoriaDetail(DetailView):
    model = models.ServicioCategoria


class ServicioCategoriaList(ListView):
    model = models.ServicioCategoria

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.ServicioCategoria.objects.filter(nombre__icontains=query)
        else:
            object_list = models.ServicioCategoria.objects.all()
        return object_list


class ServicioCategoriaCreate(CreateView):
    model = models.ServicioCategoria
    form_class = forms.ServicioCategoriaForm
    success_url = reverse_lazy("servicio:index")


class ServicioCategoriaDelete(DeleteView):
    model = models.ServicioCategoria
    success_url = reverse_lazy("servicio:serviciocategoria_list")


class ServicioCategoriaUpdate(UpdateView):
    model = models.ServicioCategoria
    success_url = reverse_lazy("servicio:serviciocategoria_list")
    form_class = forms.ServicioCategoriaForm


# *** Servicio


class ServicioCreate(CreateView):
    model = models.Servicio
    form_class = forms.ServicioForm
    success_url = reverse_lazy("servicio:index")


class ServicioList(ListView):
    model = models.Servicio

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Servicio.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Servicio.objects.all()
        return object_list


class ServicioDetail(DetailView):
    model = models.Servicio


class ServicioDelete(DeleteView):
    model = models.Servicio
    success_url = reverse_lazy("servicio:servicio_list")


class ServicioUpdate(UpdateView):
    model = models.Servicio
    success_url = reverse_lazy("servicio:servicio_list")
    form_class = forms.ServicioForm
