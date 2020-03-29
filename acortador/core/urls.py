from django.urls import path
from .views import CrearAcortador,PaginaEnlace,RedirectEnlace

app_name = 'core'

urlpatterns = [
    path('',CrearAcortador.as_view(),name='inicio'),
    path('<int:pk>/',PaginaEnlace.as_view(),name='detalle'),
    path('<str:codigo>/',RedirectEnlace.as_view(),name='redirect'),
]
