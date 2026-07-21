export const StudentTable = ({ alumnos }) => (
  <div className="card shadow-sm border-0">
    <div className="card-header bg-secondary text-white"><h5>📋 Alumnos Registrados</h5></div>
    <div className="table-responsive">
      <table className="table table-hover mb-0">
        <thead className="table-light">
          <tr>
            <th>Matrícula</th>
            <th>Nombre</th>
            <th>Correo</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {alumnos.map((a, index) => (
            <tr key={index}>
              <td>{a.matricula}</td>
              <td>{a.nombre}</td>
              <td>{a.correo}</td>
              <td>
                <button className="btn btn-outline-warning btn-sm me-2">✏️</button>
                <button className="btn btn-outline-danger btn-sm">🗑️</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  </div>
);