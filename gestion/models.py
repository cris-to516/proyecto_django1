from django.db import models

# ==========================================
# 1. TABLA: PERIODOS ESCOLARES
# ==========================================
class PeriodoEscolar(models.Model):
    clave_periodo = models.CharField(max_length=10, primary_key=True)
    nombre_periodo = models.CharField(max_length=50)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_termino = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=20, default='planeado')

    def __str__(self):
        return self.nombre_periodo

# ==========================================
# 2. TABLA: DOCENTES
# ==========================================
class Docente(models.Model):
    num_empleado = models.CharField(max_length=15, primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    correo_institucional = models.EmailField(max_length=100, unique=True)
    numero_telefonico = models.CharField(max_length=15, blank=True, null=True)
    especialidad = models.CharField(max_length=50, blank=True, null=True)
    estatus_laboral = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre_completo

# ==========================================
# 3. TABLA: CURSOS
# ==========================================
class Curso(models.Model):
    clave_curso = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    horas_semanales = models.IntegerField(blank=True, null=True)
    semestre_pertenece = models.IntegerField(blank=True, null=True)
    creditos = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# ==========================================
# 4. TABLA: ESTUDIANTE
# ==========================================
class Estudiante(models.Model):
    matricula = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50, blank=True, null=True)
    correo_electronico = models.EmailField(max_length=100, unique=True)
    numero_telefonico = models.CharField(max_length=15, blank=True, null=True)
    semestre = models.IntegerField(blank=True, null=True)
    estatus_academico = models.CharField(max_length=20, default='activo')

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno}"

# ==========================================
# 5. TABLA: GRUPOS
# ==========================================
class Grupo(models.Model):
    clave_grupo = models.CharField(max_length=10, primary_key=True)
    clave_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    num_empleado = models.ForeignKey(Docente, on_delete=models.CASCADE)
    clave_periodo = models.ForeignKey(PeriodoEscolar, on_delete=models.CASCADE)
    dias_clase = models.CharField(max_length=50, blank=True, null=True)
    aula = models.CharField(max_length=20, blank=True, null=True)
    cupo_maximo = models.IntegerField(blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_termino = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"Grupo {self.clave_grupo} - {self.clave_curso.nombre}"

# ==========================================
# 6. TABLA: INSCRIPCIONES
# ==========================================
class Inscripcion(models.Model):
    id_inscripcion = models.AutoField(primary_key=True)
    matricula = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    clave_grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='activa')
    calificacion_final = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    asistencias = models.IntegerField(default=0)
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('matricula', 'clave_grupo')

    def __str__(self):
        return f"Inscripción {self.id_inscripcion}: {self.matricula}"