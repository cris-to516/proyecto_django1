import { NavLink } from 'react-router-dom';

export const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark mb-4 shadow">
      <div className="container">
        <span className="navbar-brand fw-bold">🎓 Control Escolar</span>
        <div className="collapse navbar-collapse show">
          <ul className="navbar-nav me-auto">
            <li className="nav-item">
              <NavLink className={({ isActive }) => isActive ? "nav-link active fw-bold" : "nav-link"} to="/">Inicio</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className={({ isActive }) => isActive ? "nav-link active fw-bold" : "nav-link"} to="/listado">Listado</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className={({ isActive }) => isActive ? "nav-link active fw-bold" : "nav-link"} to="/registro">Registro</NavLink>
            </li>
            <li className="nav-item">
              <NavLink className={({ isActive }) => isActive ? "nav-link active fw-bold" : "nav-link"} to="/acerca">Acerca de</NavLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};