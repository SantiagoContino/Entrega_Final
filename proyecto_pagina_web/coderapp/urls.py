from django.urls import path
from coderapp.views import index, urban, crossover, deportivo, urban_formulario, crossover_formulario, deportivo_formulario, buscar_urban


urlpatterns = [
    path("urban/", urban, name='urban'),
    path("crossover/", crossover, name='crossover'),
    path("deportivo/", deportivo, name='deportivo'),
    path("urban_formulario/", urban_formulario, name='urban_formulario'),
    path("crossover_formulario/", crossover_formulario, name='crossover_formulario'),
    path("deportivo_formulario/", deportivo_formulario, name='deportivo_formulario'),
    path("buscar_urban/", buscar_urban, name='buscar_urban'),
    path("", index, name='index'),
]