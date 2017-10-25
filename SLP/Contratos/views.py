from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
# Create your views here.
from django.core.urlresolvers import reverse
from django.shortcuts import render
from.form import registrarplaza


from django.views.generic import (
        CreateView,
        ListView,
        UpdateView,
        DeleteView,
        DetailView
    )
from.models import (
    CatContinente,
    CatEstados,
    CatPais,
    CatPlaza,
)


class RegistrarPlaza(CreateView):
    model = CatPlaza
    form_class = registrarplaza
    template_name = "form_plaza.html"
    success_url = reverse_lazy("Plazas:editar")

class EditarPlaza(ListView):
    model = CatPlaza
    queryset = CatPlaza.objects.all()
    form_class = registrarplaza
    context_object_name = "plz"
    template_name = "form_editar.html"

class ActualizarPlaza(UpdateView):
     model = CatPlaza
     pk_url_kwarg = "pk"
     context_object_name = "plazas"
     form_class = registrarplaza
     success_url = reverse_lazy("Plazas:editar")
     template_name = "EditarPlaza.html"

class EliminarPlaza(DeleteView):
    model = CatPlaza
    pk_url_kwarg = "pk"
    context_object_name = "plaza"
    template_name = "eliminar_palza.html"
    success_url = reverse_lazy("Plazas:editar")

class DetallesPlaza(DetailView):
    model = CatPlaza
    pk_url_kwarg = "pk"
    context_object_name = "plaz"
    template_name = "Detalles.html"