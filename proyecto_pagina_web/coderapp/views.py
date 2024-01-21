from django.http import HttpResponse
from django.shortcuts import render

from coderapp.models import Urban, Crossover, Deportivo
from coderapp.forms import UrbanFormulario, CrossoverFormulario, DeportivoFormulario

def index(request):
    return render(request, "index.html")

def urban(request):
    autos = Urban.objects.all

    contexto= {"autos":autos}
    return render(request, 'urban.html', contexto)

def crossover(request):
    autos = Crossover.objects.all

    contexto= {"autos":autos}
    return render(request, 'crossover.html', contexto)

def deportivo(request):
    autos = Deportivo.objects.all

    contexto= {"autos":autos}
    return render(request, 'deportivo.html', contexto)

def urban_formulario(request):
    
    if request.method == "POST":
       
        formulario = UrbanFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            marca = datos.get('marca')
            modelo = datos.get('modelo')
            año = datos.get('año')

            auto = Urban(marca=marca, modelo=modelo, año=año)
            auto.save()

            return render(request, 'index.html')
    else:
        formulario = UrbanFormulario()
        
    return render(request, 'urban_formulario.html', {'formulario': formulario})


def crossover_formulario(request):
    
    if request.method == "POST":
       
        formulario = CrossoverFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            marca = datos.get('marca')
            modelo = datos.get('modelo')
            año = datos.get('año')

            auto = Crossover(marca=marca, modelo=modelo, año=año)
            auto.save()

            return render(request, 'index.html')
    else:
        formulario = CrossoverFormulario()
        
    return render(request, 'crossover_formulario.html', {'formulario': formulario})


def deportivo_formulario(request):
    
    if request.method == "POST":
       
        formulario = DeportivoFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            marca = datos.get('marca')
            modelo = datos.get('modelo')
            año = datos.get('año')

            auto = Deportivo(marca=marca, modelo=modelo, año=año)
            auto.save()

            return render(request, 'index.html')
    else:
        formulario = DeportivoFormulario()
        
    return render(request, 'deportivo_formulario.html', {'formulario': formulario})

def buscar_urban(request):
    if request.method == "GET":
        modelo = request.GET.get("modelo")

        if modelo is None:
            return HttpResponse("No ingresó ningún modelo")
        modelos = Urban.objects.filter(modelo__icontains=modelo)
        
        contexto= {
            "modelos": modelos,
        }

        return render(request, "buscar_urban.html", contexto)

