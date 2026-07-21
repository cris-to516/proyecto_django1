from rest_framework import viewsets  # <-- ESTA LÍNEA ES LA QUE FALTA
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Inicializamos el router para la API REST
router = DefaultRouter()
router.register(r'estudiantes-api', views.EstudianteViewSet, basename='estudiante-api')

urlpatterns = [
    # 1. Rutas del CRUD clásico (Interfaz Web)
    path('', views.lista_estudiantes, name='inicio'),
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/nuevo/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/editar/<str:matricula>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<str:matricula>/', views.eliminar_estudiante, name='eliminar_estudiante'),
    
    # 2. Ruta de la API REST automatizada
    path('api/', include(router.urls)),
]