# Lista de Verificación de Seguridad, Respaldo y Monitoreo
**Proyecto:** PROYECTO_DJANGO1 (Django + React)

| N° | Criterio a Verificar | Estado | Observación / Aplicación en el Proyecto |
|---|---|---|---|
| 1 | **Contraseñas seguras** | ✅ Cumple | Django gestiona el hashing de contraseñas de usuarios por defecto mediante algoritmos seguros (PBKDF2). |
| 2 | **Variables de entorno** | ✅ Cumple | La clave `SECRET_KEY` de Django y credenciales sensibles se manejan separadas en variables de entorno o archivo de configuración local. |
| 3 | **Acceso restringido** | ✅ Cumple | Rutas del backend protegidas por autenticación (decoradores/permisos en Django) y el panel `/admin` restringido a superusuarios. |
| 4 | **Copias de seguridad** | ✅ Cumple | Respaldo y copia de la base de datos `db.sqlite3` realizado correctamente. |
| 5 | **Registro de errores** | ✅ Cumple | Configuración de logs activa en Django (`LOGGING` en `settings.py`) o consola de ejecución. |
| 6 | **Disponibilidad del servicio** | ✅ Cumple | Servidores de desarrollo ejecutándose activamente (`manage.py runserver` y `npm run dev`). |
| 7 | **Uso de HTTPS** | ⚠️ Pendiente | En desarrollo se utiliza HTTP (`localhost`). Configuración SSL/HTTPS lista para entorno de producción. |
| 8 | **Protección de archivos** | ✅ Cumple | Archivo `.gitignore` configurado para excluir `db.sqlite3`, `venv/`, `node_modules/` y entornos virtuales. |
| 9 | **Permisos de usuarios** | ✅ Cumple | Roles definidos en Django Admin (administradores vs usuarios estándar). |
| 10 | **Actualización de dependencias**| ✅ Cumple | Paquetes de Node (`package.json`) y Python (`requirements.txt` / `venv`) verificados sin vulnerabilidades activas. |