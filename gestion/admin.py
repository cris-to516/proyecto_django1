from django.contrib import admin
from .models import PeriodoEscolar, Docente, Curso, Estudiante, Grupo, Inscripcion

# Personalización del modelo Estudiante
@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nombre', 'apellido_paterno', 'correo_electronico', 'semestre', 'estatus_academico')
    search_fields = ('matricula', 'nombre', 'apellido_paterno')
    list_filter = ('semestre', 'estatus_academico')

# Personalización del modelo Curso
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('clave_curso', 'nombre', 'horas_semanales', 'creditos')
    search_fields = ('clave_curso', 'nombre')

# Personalización del modelo Inscripcion (Relaciones)
@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id_inscripcion', 'matricula', 'clave_grupo', 'calificacion_final', 'asistencias', 'estado')
    list_filter = ('estado', 'clave_grupo')

# Registrar los demás modelos de forma básica
admin.site.register(PeriodoEscolar)
admin.site.register(Docente)
admin.site.register(Grupo)