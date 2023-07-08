from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="servicio/index.html"), name="index"),
    path("serviciocategoria/detail/<int:pk>", views.ServicioCategoriaDetail.as_view(), name="serviciocategoria_detail"),
    path("serviciocategoria/list/", views.ServicioCategoriaList.as_view(), name="serviciocategoria_list"),
    path("serviciocategoria/create/", staff_member_required(views.ServicioCategoriaCreate.as_view()), name="serviciocategoria_create"),
    path("serviciocategoria/delete/<int:pk>", staff_member_required(views.ServicioCategoriaDelete.as_view()), name="serviciocategoria_delete"),
    path("serviciocategoria/update/<int:pk>", staff_member_required(views.ServicioCategoriaUpdate.as_view()), name="serviciocategoria_update"),
    path("servicio/detail/<int:pk>", views.ServicioDetail.as_view(), name="servicio_detail"),
    path("servicio/list/", views.ServicioList.as_view(), name="servicio_list"),
    path("servicio/create/", staff_member_required(views.ServicioCreate.as_view()), name="servicio_create"),
    path("servicio/delete/<int:pk>", staff_member_required(views.ServicioDelete.as_view()), name="servicio_delete"),
    path("servicio/update/<int:pk>", staff_member_required(views.ServicioUpdate.as_view()), name="servicio_update"),
]
