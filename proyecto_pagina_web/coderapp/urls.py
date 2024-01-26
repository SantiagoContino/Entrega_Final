from django.urls import path
from django.contrib.auth.views import LogoutView
from coderapp.views import index, urban, crossover, deportivo, urban_formulario, crossover_formulario, deportivo_formulario, buscar_urban, eliminar_urban, eliminar_crossover, eliminar_deportivo, editar_urban, editar_crossover, editar_deportivo, login_request, registrar


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
    path("editar_urban/<modelo_urban>/", editar_urban, name='editar_urban'), 
    path("editar_crossover/<modelo_crossover>/", editar_crossover, name='editar_crossover'), 
    path("editar_deportivo/<modelo_deportivo>/", editar_deportivo, name='editar_deportivo'), 
    path("login", login_request, name='login'),
    path("registrar", registrar, name='registrar'),
    path("logout", LogoutView.as_view(template_name="logout.html"), name='logout'),
    path("", index, name='index'),
]