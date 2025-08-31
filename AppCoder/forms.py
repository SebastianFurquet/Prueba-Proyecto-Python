from django import forms
from .models import Estudiante

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    

class BusquedaEstudianteForm(forms.Form):
    apellido = forms.CharField(max_length=100)