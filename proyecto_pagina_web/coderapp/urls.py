from django.urls import path
from coderapp.views import index, urban, crossover, deportivo, urban_formulario, crossover_formulario, deportivo_formulario, buscar_urban, eliminar_urban, eliminar_crossover, eliminar_deportivo


urlpatterns = [
    path("urban/", urban, name='urban'),
    path("crossover/", crossover, name='crossover'),
    path("deportivo/", deportivo, name='deportivo'),
    path("urban_formulario/", urban_formulario, name='urban_formulario'),
    path("crossover_formulario/", crossover_formulario, name='crossover_formulario'),
    path("deportivo_formulario/", deportivo_formulario, name='deportivo_formulario'),
    path("buscar_urban/", buscar_urban, name='buscar_urban'),
    path("eliminar_urban/<modelo_urban>/", eliminar_urban, name='eliminar_urban'),
    path("eliminar_crossover/<modelo_crossover>/", eliminar_crossover, name='eliminar_crossover'),
    path("eliminar_urban/<modelo_deportivo>/", eliminar_deportivo, name='eliminar_deportivo'),
    path("", index, name='index'),
]