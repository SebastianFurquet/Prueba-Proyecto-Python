from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:pk>/', views.detalle_estudiante, name='detalle_estudiante'),
    path("estudiantes/form/", views.estudiantes_form, name="estudiantes_form"),
    path('buscarEstudiante/', views.buscarEstudiante, name='buscarEstudiante'),
]