from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView

from .forms import AcortadorForm
from .models import Enlace

# Create your views here.
#vamos apoyarnos del siguente link para las vista basadas en clases:
#https://ccbv.co.uk/projects/Django/2.2/



class CrearAcortador(CreateView):
    model = Enlace
    form_class = AcortadorForm
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs) #renderiza cada elemento en forma de diccionario
        contexto['total_enlaces'] = Enlace.enlaces.total_enlaces()
        contexto['total_redirecciones'] = Enlace.enlaces.total_redirecciones()['redirecciones']
        return contexto


class PaginaEnlace(DetailView):
    model = Enlace
    template_name = "enlace.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['marzo'] = Enlace.enlaces.fechas(self.kwargs['pk'])[0]['marzo']
        return contexto
    

class RedirectEnlace(RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        try:
            return Enlace.enlaces.decode_enlace(self.kwargs['codigo'])
        except IndexError:
            print("Decode sin datos")