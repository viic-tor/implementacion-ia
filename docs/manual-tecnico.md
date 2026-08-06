## Arquitectura
El flujo inicia cuando un cliente (Navegador o Postman) envía una petición HTTP a la API FastAPI en el puerto 8000. FastAPI procesa la solicitud mediante dos rutas posibles: el motor `eco` (reglas estáticas) o el motor `ollama` (modelo local en el puerto 11434). El resultado de la clasificación se guarda en una base de datos PostgreSQL expuesta en el puerto 5432 y, finalmente, se devuelve la respuesta en formato JSON al cliente.

## Seguridad
- **Puertos expuestos:** La API expone el puerto 8000. PostgreSQL se expone en el 5432 solo para el backend.
- **Roles de base de datos:** Se utiliza el rol `app_ia` con privilegios mínimos limitados exclusivamente a `SELECT` e `INSERT`. No tiene permisos para modificar ni borrar datos (DROP, DELETE).
- **Manejo de secretos:** Todas las credenciales se administran mediante un archivo `.env` local que está ignorado en Git (`.gitignore`), previniendo fugas de contraseñas.

