from django.shortcuts import render
from .models import Auto
from .forms import FormularioCreacionAuto
# Create your views here.

def funcion(request):
    return render(request, 'aplicacion/html' , {'contexto': 'Hola Mundo'})

#---------------------------------------------------------------------

def index(request):
    return render(request, 'AppCoder/index.html')


def crear_auto_v2(request):
    
    formulario = FormularioCreacionAuto() # creamos un objeto del formulario
    
    return render(request, 'AppCoder/crear_auto_v2.html', {'formulario': formulario} )