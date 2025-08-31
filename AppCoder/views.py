from django.shortcuts import render, redirect, get_list_or_404
from .models import Estudiante, Profesor, Curso, Entregable
from .forms import EstudianteForm, BusquedaEstudianteForm

def index(request):
    return render(request, 'AppCoder/index.html')


def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'AppCoder/lista_estudiantes.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_list_or_404(Estudiante, pk=pk)
    return render(request, 'AppCoder/estudiantes_detail.html', {'estudiante':estudiante})

def estudiantes_form(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            estudiantes = Estudiante(nombre=nombre, apellido=apellido,email=email)
            estudiantes.save()
            return redirect('lista_estudiantes')
        
    else: form = EstudianteForm()
    return render(request, 'AppCoder/estudiantes_form.html', {'form': form})



def buscarEstudiante(request): 
    if request.method == 'GET': 
        form = BusquedaEstudianteForm(request.GET) 
        if form.is_valid(): 
            apellido = form.cleaned_data['apellido'] 
            resultados = Estudiante.objects.filter(apellido=apellido) 
            return render(request, 'AppCoder/resultados_busqueda.html', {'resultados': resultados, 'form': form}) 
        
    else: form = BusquedaEstudianteForm() 
    return render(request, 'AppCoder/buscarEstudiante.html', {'form': form})