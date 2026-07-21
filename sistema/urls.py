# sistema/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gestion import views

# Inicializamos el router de Django REST Framework
router = DefaultRouter()
router.register(r'estudiantes-api', views.EstudianteViewSet, basename='estudiante-api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Aquí se registran las rutas del CRUD
    
    # ESTA LÍNEA AGREGA EL INICIO/CIERRE DE SESIÓN EN LA INTERFAZ DE LA API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]