from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from rest_framework import viewsets  # <-- Ponemos la importación aquí arriba
from .models import Estudiante
from .forms import EstudianteForm
from .serializers import EstudianteSerializer  # <-- Importamos tu serializador aquí

# 1. Vista de consulta (Lista con Bootstrap)
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'gestion/estudiantes.html', {'estudiantes': estudiantes})

# 2. Formulario de alta (Crear)
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Estudiante registrado con éxito!')
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'gestion/formulario.html', {'form': form, 'titulo': 'Formulario de Alta'})

# 3. Formulario de modificación (Editar)
def editar_estudiante(request, matricula):
    estudiante = get_object_or_404(Estudiante, matricula=matricula)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro actualizado correctamente!')
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'gestion/formulario.html', {'form': form, 'titulo': 'Modificar Estudiante'})

# 4. Confirmación de eliminación (Borrar)
def eliminar_estudiante(request, matricula):
    estudiante = get_object_or_404(Estudiante, matricula=matricula)
    if request.method == 'POST':
        estudiante.delete()
        messages.success(request, 'Estudiante eliminado del sistema.')
        return redirect('lista_estudiantes')
    return render(request, 'gestion/confirmar_eliminar.html', {'estudiante': estudiante})

# 5. NUEVA VISTA PARA LA API REST (Fuera de las funciones anteriores)
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

    # gestion/views.py
from rest_framework import viewsets
from .models import Estudiante
from .serializers import EstudianteSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer