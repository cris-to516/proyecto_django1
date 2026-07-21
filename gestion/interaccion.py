# ==========================================
# CONFIGURACIÓN INICIAL DE DJANGO (OBLIGATORIA)
# ==========================================
import os
import django

# Indicamos a Python cuál es el archivo de configuración de nuestro proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema.settings')
django.setup()

# Importamos las clases de nuestras tablas de MySQL convertidas a Django
from gestion.models import PeriodoEscolar, Docente, Curso, Estudiante, Grupo, Inscripcion
from datetime import date, time

print("--- INICIANDO PRUEBAS DE INTERACCIÓN CON LA BASE DE DATOS ---\n")

# ==========================================
# 1. INSERCIÓN DE DATOS DE PRUEBA (CREATE)
# ==========================================
print("[+] Registrando datos de prueba...")

# Insertar un Periodo Escolar
periodo, _ = PeriodoEscolar.objects.get_or_create(
    clave_periodo="2026-A",
    defaults={'nombre_periodo': 'Primer Semestre 2026', 'estado': 'activo'}
)

# Insertar un Docente
docente, _ = Docente.objects.get_or_create(
    num_empleado="DOC-001",
    defaults={'nombre_completo': 'Mtro. Aldo Alvarez Jurado', 'correo_institucional': 'aldo.alvarez@cet.edu.mx'}
)

# Insertar un Curso
curso, _ = Curso.objects.get_or_create(
    clave_curso="CUR-01",
    defaults={'nombre': 'Aplicaciones Informaticas', 'horas_semanales': 5, 'creditos': 8}
)

# Insertar dos Estudiantes (Aby, Salvador y Cristopher)
estudiante1, _ = Estudiante.objects.get_or_create(
    matricula="EST-001",
    defaults={'nombre': 'Aby', 'apellido_paterno': 'Corona', 'correo_electronico': 'aby.corona@cet.edu.mx', 'semestre': 3}
)

estudiante2, _ = Estudiante.objects.get_or_create(
    matricula="EST-002",
    defaults={'nombre': 'Salvador', 'apellido_paterno': 'Ramirez', 'correo_electronico': 'salvador.ramirez@cet.edu.mx', 'semestre': 3}
)

# Insertar un Grupo relacionando Curso, Docente y Periodo (Llaves Foráneas)
grupo, _ = Grupo.objects.get_or_create(
    clave_grupo="GRP-301",
    defaults={
        'clave_curso': curso,
        'num_empleado': docente,
        'clave_periodo': periodo,
        'aula': 'Laboratorio A',
        'cupo_maximo': 30
    }
)

# Inscribir a los estudiantes al grupo
Inscripcion.objects.get_or_create(matricula=estudiante1, clave_grupo=grupo, defaults={'asistencias': 12, 'calificacion_final': 9.50})
Inscripcion.objects.get_or_create(matricula=estudiante2, clave_grupo=grupo, defaults={'asistencias': 15, 'calificacion_final': 10.00})

print("✓ Datos base creados correctamente.\n")

# ==========================================
# 2. CONSULTA DE REGISTROS (READ)
# ==========================================
print("[+] Ejecutando consultas en las tablas...")

# Consultar todos los estudiantes inscritos
alumnos = Estudiante.objects.all()
print(f"-> Total de alumnos registrados en el sistema: {alumnos.count()}")
for al en alumnos:
    print(f"   * Matrícula: {al.matricula} | Nombre: {al.nombre} {al.apellido_paterno} | Estatus: {al.estatus_academico}")

# Consultar las inscripciones y calificaciones asociadas
print("\n-> Lista de calificaciones en el grupo GRP-301:")
inscripciones = Inscripcion.objects.filter(clave_grupo=grupo)
for ins in inscripciones:
    print(f"   * Alumno: {ins.matricula.nombre} | Calificación: {ins.calificacion_final} | Asistencias: {ins.asistencias}")

print("\n--- FINALIZACIÓN DE SCRIPT CON ÉXITO ---")