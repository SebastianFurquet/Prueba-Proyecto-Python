from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('crear-auto/<marca>/<modelo>', views.crear_auto , name='crear_auto'),
    path('auto/crear/', views.crear_auto_v2 , name='crear_auto')
    
]
