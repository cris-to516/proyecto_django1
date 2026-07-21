import React, { useState, useEffect } from 'react';

function App() {
  // Estados principales
  const [estudiantes, setEstudiantes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Estado del formulario
  const [form, setForm] = useState({ matricula: '', nombre: '', correo: '' });

  const API_URL = 'http://127.0.0.1:8000/api/estudiantes/';

  // 1. OBTENER REGISTROS (GET)
  const obtenerEstudiantes = async () => {
    try {
      setLoading(true);
      const res = await fetch(API_URL);
      if (!res.ok) throw new Error('Error al conectar con la API');
      const data = await res.json();
      setEstudiantes(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    obtenerEstudiantes();
  }, []);

  // 2. CREAR UN REGISTRO (POST)
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!form.matricula || !form.nombre || !form.correo) {
      alert('⚠️ Por favor completa todos los campos.');
      return;
    }

    try {
      const res = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      });

      if (res.ok) {
        const nuevoEstudiante = await res.json();
        // Optimización del estado agregando el nuevo elemento
        setEstudiantes([...estudiantes, nuevoEstudiante]);
        setForm({ matricula: '', nombre: '', correo: '' });
      }
    } catch (err) {
      alert('❌ Error al guardar el registro');
    }
  };

  // 3. ELIMINAR UN REGISTRO (DELETE) Y OPTIMIZAR ESTADO
  const handleElimINAR = async (id, nombre) => {
    // Confirmación previa de seguridad antes de eliminar
    const confirmar = window.confirm(`¿Estás seguro de que deseas eliminar a ${nombre}?`);
    if (!confirmar) return;

    try {
      const res = await fetch(`${API_URL}${id}/`, {
        method: 'DELETE'
      });

      if (res.ok || res.status === 204) {
        // Optimización del estado: Filtramos en memoria sin hacer otra consulta HTTP
        setEstudiantes(estudiantes.filter(est => est.id !== id));
        console.log(`✅ Estudiante con ID ${id} eliminado correctamente.`);
      } else {
        alert('❌ No se pudo eliminar el estudiante del servidor.');
      }
    } catch (err) {
      console.error('Error al eliminar:', err);
      alert('⚠️ Ocurrió un error al intentar eliminar.');
    }
  };

  return (
    <div className="container mt-4 mb-5">
      <header className="pb-3 mb-4 border-bottom">
        <h1 className="h2 text-primary fw-bold">🎓 Sistema de Gestión Escolar - CRUD React</h1>
      </header>

      <div className="row g-4">
        {/* COLUMNA FORMULARIO */}
        <div className="col-lg-4">
          <div className="card shadow-sm border-0">
            <div className="card-header bg-primary text-white fw-bold">
              📝 Registrar Estudiante
            </div>
            <div className="card-body">
              <form onSubmit={handleSubmit}>
                <div className="mb-3">
                  <label className="form-label">Matrícula</label>
                  <input
                    type="text"
                    className="form-control"
                    value={form.matricula}
                    onChange={(e) => setForm({ ...form, matricula: e.target.value })}
                    placeholder="Ej. 2026001"
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Nombre Completo</label>
                  <input
                    type="text"
                    className="form-control"
                    value={form.nombre}
                    onChange={(e) => setForm({ ...form, nombre: e.target.value })}
                    placeholder="Ej. Juan Pérez"
                  />
                </div>
                <div className="mb-3">
                  <label className="form-label">Correo Electrónico</label>
                  <input
                    type="email"
                    className="form-control"
                    value={form.correo}
                    onChange={(e) => setForm({ ...form, correo: e.target.value })}
                    placeholder="correo@ejemplo.com"
                  />
                </div>
                <button type="submit" className="btn btn-primary w-100 fw-bold">
                  ➕ Agregar Estudiante
                </button>
              </form>
            </div>
          </div>
        </div>

        {/* COLUMNA TABLA CON BOTÓN DE ELIMINAR */}
        <div className="col-lg-8">
          <div className="card shadow-sm border-0">
            <div className="card-header bg-dark text-white fw-bold">
              📋 Lista de Alumnos
            </div>
            <div className="card-body p-0">
              {loading && <p className="p-3 text-muted">Cargando alumnos...</p>}
              {error && <p className="p-3 text-danger">Error: {error}</p>}

              {!loading && !error && (
                <div className="table-responsive">
                  <table className="table table-hover align-middle mb-0">
                    <thead className="table-light">
                      <tr>
                        <th>ID</th>
                        <th>Matrícula</th>
                        <th>Nombre</th>
                        <th>Correo</th>
                        <th className="text-center">Acciones</th>
                      </tr>
                    </thead>
                    <tbody>
                      {estudiantes.length === 0 ? (
                        <tr>
                          <td colSpan="5" className="text-center p-3 text-muted">
                            No hay registros.
                          </td>
                        </tr>
                      ) : (
                        // Asignación de propiedad key única utilizando el ID
                        estudiantes.map((est) => (
                          <tr key={est.id}>
                            <td>{est.id}</td>
                            <td><span className="badge bg-secondary">{est.matricula}</span></td>
                            <td className="fw-semibold">{est.nombre}</td>
                            <td>{est.correo}</td>
                            <td className="text-center">
                              <button
                                className="btn btn-outline-danger btn-sm"
                                onClick={() => handleElimINAR(est.id, est.nombre)}
                              >
                                🗑️ Eliminar
                              </button>
                            </td>
                          </tr>
                        ))
                      )}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;