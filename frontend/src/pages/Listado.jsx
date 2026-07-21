import React, { useState, useEffect } from 'react';

export const Listado = () => {
  // Estados para almacenar datos, estado de carga y errores
  const [estudiantes, setEstudiantes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // 1. Configuración de la URL de la API del Backend (Django)
  const API_URL = 'http://127.0.0.1:8000/api/estudiantes/'; 

  useEffect(() => {
    // 2. Realizar la solicitud GET mediante fetch
    const obtenerEstudiantes = async () => {
      try {
        setLoading(true);
        setError(null);

        const response = await fetch(API_URL);

        if (!response.ok) {
          throw new Error(`Error en la petición: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        
        // 6. Verificar la respuesta en la consola del navegador
        console.log('✅ Respuesta obtenida de la API:', data);

        // 3. Almacenar la respuesta en el estado
        setEstudiantes(data);
      } catch (err) {
        console.error('❌ Error al consultar la API:', err.message);
        setError('No se pudo conectar con el backend. Verifique que Django esté encendido.');
      } finally {
        setLoading(false);
      }
    };

    obtenerEstudiantes();
  }, []);

  return (
    <div className="container mt-4">
      <h2 className="mb-4 text-primary">📋 Consulta de Estudiantes (API GET)</h2>

      {/* 5. MENSAJE DE CARGA */}
      {loading && (
        <div className="alert alert-info d-flex align-items-center role="alert"">
          <div className="spinner-border spinner-border-sm me-2" role="status"></div>
          <div>Cargando datos desde el servidor... Por favor espere.</div>
        </div>
      )}

      {/* 5. MENSAJE DE ERROR */}
      {error && (
        <div className="alert alert-danger" role="alert">
          <strong>⚠️ Error:</strong> {error}
        </div>
      )}

      {/* 5. MENSAJE CUANDO NO EXISTAN REGISTROS */}
      {!loading && !error && estudiantes.length === 0 && (
        <div className="alert alert-warning" role="alert">
          📌 No existen registros de estudiantes en la base de datos.
        </div>
      )}

      {/* 4. MOSTRAR LA INFORMACIÓN EN UNA TABLA */}
      {!loading && !error && estudiantes.length > 0 && (
        <div className="card shadow-sm border-0">
          <div className="card-header bg-dark text-white fw-bold">
            Lista de Alumnos Obtenidos de la API
          </div>
          <div className="table-responsive">
            <table className="table table-hover align-middle mb-0">
              <thead className="table-light">
                <tr>
                  <th># ID</th>
                  <th>Matrícula</th>
                  <th>Nombre</th>
                  <th>Correo</th>
                </tr>
              </thead>
              <tbody>
                {estudiantes.map((est, index) => (
                  <tr key={est.id || index}>
                    <td>{est.id || index + 1}</td>
                    <td><span className="badge bg-secondary">{est.matricula || 'N/A'}</span></td>
                    <td className="fw-semibold">{est.nombre}</td>
                    <td>{est.correo}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
};

export default Listado;