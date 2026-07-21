import React, { useState } from 'react';

export const StudentForm = ({ onAdd }) => {
  const [estudiante, setEstudiante] = useState({ matricula: '', nombre: '', correo: '' });

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!estudiante.matricula || !estudiante.nombre || !estudiante.correo) {
      alert("⚠️ Por favor, llena todos los campos.");
      return;
    }
    onAdd(estudiante); // Enviar datos al componente padre
    setEstudiante({ matricula: '', nombre: '', correo: '' }); // Limpiar
  };

  return (
    <div className="card shadow-sm border-0">
      <div className="card-header bg-primary text-white"><h5>📝 Registro de Estudiante</h5></div>
      <div className="card-body">
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <input type="text" className="form-control" placeholder="Matrícula" 
              value={estudiante.matricula} onChange={(e) => setEstudiante({...estudiante, matricula: e.target.value})} />
          </div>
          <div className="mb-3">
            <input type="text" className="form-control" placeholder="Nombre completo" 
              value={estudiante.nombre} onChange={(e) => setEstudiante({...estudiante, nombre: e.target.value})} />
          </div>
          <div className="mb-3">
            <input type="email" className="form-control" placeholder="Correo electrónico" 
              value={estudiante.correo} onChange={(e) => setEstudiante({...estudiante, correo: e.target.value})} />
          </div>
          <button type="submit" className="btn btn-primary w-100 fw-bold">Agregar a la Lista</button>
        </form>
      </div>
    </div>
  );
};