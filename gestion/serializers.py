# gestion/serializers.py
from rest_framework import serializers
from .models import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'  # Esto tomará automáticamente matricula, nombre, correo, etc.