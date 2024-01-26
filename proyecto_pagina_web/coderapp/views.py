from django.http import HttpResponse
from django.shortcuts import render

from coderapp.models import Urban, Crossover, Deportivo
from coderapp.forms import UrbanFormulario, CrossoverFormulario, DeportivoFormulario

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

@login_required
def urban(request):
    autos = Urban.objects.all

    contexto= {"autos":autos}
    return render(request, 'urban.html', contexto)

@login_required
def crossover(request):
    autos = Crossover.objects.all

    contexto= {"autos":autos}
    return render(request, 'crossover.html', contexto)

@login_required
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

def eliminar_urban(request, modelo_urban):
     
     urban = Urban.objects.get(modelo=modelo_urban)

     urban.delete()

     autos = Urban.objects.all()
     contexto = {"autos":autos}

     return render(request, 'urban.html', contexto)


def eliminar_crossover(request, modelo_crossover):
     
     crossover = Crossover.objects.get(modelo=modelo_crossover)

     crossover.delete()

     autos = Crossover.objects.all()
     contexto = {"autos":autos}

     return render(request, 'crossover.html', contexto)


def eliminar_deportivo(request, modelo_deportivo):
     
     deportivo = Deportivo.objects.get(modelo=modelo_deportivo)

     deportivo.delete()

     autos = Deportivo.objects.all()
     contexto = {"autos":autos}

     return render(request, 'deportivo.html', contexto)


def editar_urban(request, modelo_urban):

    urban = Urban.objects.get(modelo=modelo_urban)

    if request.method == "POST":
        formulario = UrbanFormulario(request.POST)
        if formulario.is_valid():
            
            datos_urban = formulario.cleaned_data

            urban.marca = datos_urban.get("marca")
            urban.modelo = datos_urban.get("modelo")
            urban.año = datos_urban.get("año")

            urban.save()

            return render(request, "index.html")

    formulario = UrbanFormulario(initial={"marca":urban.marca, "modelo":urban.modelo, "año":urban.año})

    return render(request, "editar_urban.html", {"formulario":formulario, "modelo_urban": modelo_urban})


def editar_crossover(request, modelo_crossover):

    crossover = Crossover.objects.get(modelo=modelo_crossover)

    if request.method == "POST":
        formulario = CrossoverFormulario(request.POST)
        if formulario.is_valid():
            
            datos_crossover = formulario.cleaned_data

            crossover.marca = datos_crossover.get("marca")
            crossover.modelo = datos_crossover.get("modelo")
            crossover.año = datos_crossover.get("año")

            crossover.save()

            return render(request, "index.html")

    formulario = CrossoverFormulario(initial={"marca":crossover.marca, "modelo":crossover.modelo, "año":crossover.año})

    return render(request, "editar_crossover.html", {"formulario":formulario, "modelo_crossover": modelo_crossover})


def editar_deportivo(request, modelo_deportivo):

    deportivo = Deportivo.objects.get(modelo=modelo_deportivo)

    if request.method == "POST":
        formulario = DeportivoFormulario(request.POST)
        if formulario.is_valid():
            
            datos_deportivo = formulario.cleaned_data

            deportivo.marca = datos_deportivo.get("marca")
            deportivo.modelo = datos_deportivo.get("modelo")
            deportivo.año = datos_deportivo.get("año")

            deportivo.save()

            return render(request, "index.html")

    formulario = DeportivoFormulario(initial={"marca":deportivo.marca, "modelo":deportivo.modelo, "año":deportivo.año})

    return render(request, "editar_deportivo.html", {"formulario":formulario, "modelo_deportivo": modelo_deportivo})


def login_request(request):

    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return render(request, 'index.html', {"mensaje": f"Bienvenido {username}"})
            else:
                return render(request, 'index.html', {"mensaje": f"Usuario o contraseña invalidos"})
            
        else:
            return render(request, 'index.html', {"mensaje": "Los datos ingresados son incorrectos"})


    formulario = AuthenticationForm()

    return render(request, "login.html", {"formulario":formulario})


def registrar(request):

    if request.method == "POST":
        
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():

            username = formulario.cleaned_data.get("username")

            formulario.save()

            return render(request, "index.html", {"mensaje": f"el usuario {username}, ha sido dado de alta"})

    formulario = UserCreationForm()

    return render(request, "registro.html", {"formulario": formulario})


def sobre_mi(request):
    return render(request, "sobre_mi.html")