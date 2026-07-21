from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Estudiante

class EstudianteAPITests(APITestCase):

    def setUp(self):
        # Creamos un estudiante base para usar en las pruebas
        self.estudiante_base = Estudiante.objects.create(
            matricula="20260001",
            nombre="Juan",
            apellido_paterno="Pérez",
            correo_electronico="juan@oycecytem.mx",
            semestre=5,
            estatus_academico="activo"
        )
        # Ruta del endpoint
        self.url_listado = reverse('estudiante-api-list')  # Raíz de la API
        self.url_detalle = reverse('estudiante-api-detail', kwargs={'pk': self.estudiante_base.matricula})

    # --- 1. Verificación de creación de un modelo ---
    def test_creacion_modelo_estudiante(self):
        estudiante = Estudiante.objects.get(matricula="20260001")
        self.assertEqual(estudiante.nombre, "Juan")
        self.assertEqual(estudiante.apellido_paterno, "Pérez")

    # --- 2. Verificación de acceso a una vista ---
    def test_acceso_vista_listado(self):
        response = self.client.get(self.url_listado)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # --- 3. Verificación de respuesta de un endpoint ---
    def test_respuesta_endpoint_detalle(self):
        response = self.client.get(self.url_detalle)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], "Juan")