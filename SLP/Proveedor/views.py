from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
# Create your views here.
from django.core.urlresolvers import reverse
from django.shortcuts import render
from.form import proveedores


from django.views.generic import (
        CreateView,
        ListView,
        UpdateView,
        DeleteView,
        DetailView
    )
from Web.models import (
   DatProveedor
)


class RegistrarPlaza(CreateView):
    model = DatProveedor
    form_class = proveedores
    template_name = "Agregar.html"
    success_url = reverse_lazy("Proveedor:EditarProveedor")

class EditarPlaza(ListView):
    model = DatProveedor
    queryset = DatProveedor.objects.all()
    form_class = proveedores
    context_object_name = "proveedor"
    template_name = "Proveedores.html"

class ActualizarPlaza(UpdateView):
     model = DatProveedor
     pk_url_kwarg = "pk"
     context_object_name = "provee"
     form_class = proveedores
     success_url = reverse_lazy("Proveedor:Editar")
     template_name = "Editar.html"

class EliminarPlaza(DeleteView):
    model = DatProveedor
    pk_url_kwarg = "pk"
    context_object_name = "pro"
    template_name = "Eliminar.html"
    success_url = reverse_lazy("Proveedor:Proveedores")

class DetallesPlaza(DetailView):
    model = DatProveedor
    pk_url_kwarg = "pk"
    context_object_name = "prov"
    template_name = "Ver.html"