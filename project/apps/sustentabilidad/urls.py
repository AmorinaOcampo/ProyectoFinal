from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="sustentabilidad/index.html"), name="index"),
    path("sustentabilidad/list/", views.SustentabilidadList.as_view(), name="sustentabilidad_list"),
    path("sustentabilidad/detail/<int:pk>", views.SustentabilidadDetail.as_view(), name="sustentabilidad_detail"),
    path("sustentabilidad/create/", staff_member_required(views.SustentabilidadCreate.as_view()), name="sustentabilidad_create"),
    path("sustentabilidad/delete/<int:pk>", staff_member_required(views.SustentabilidadDelete.as_view()), name="sustentabilidad_delete"),
    path("sustentabilidad/update/<int:pk>", staff_member_required(views.SustentabilidadUpdate.as_view()), name="sustentabilidad_update"),
]
