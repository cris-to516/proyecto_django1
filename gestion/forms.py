from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['matricula', 'nombre', 'apellido_paterno', 'apellido_materno', 'correo_electronico', 'numero_telefonico', 'semestre', 'estatus_academico']
        widgets = {
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'numero_telefonico': forms.TextInput(attrs={'class': 'form-control'}),
            'semestre': forms.NumberInput(attrs={'class': 'form-control'}),
            'estatus_academico': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'activo'}),
        }