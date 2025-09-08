# PythonJsonSchemaLogin
## API de Autenticación

Un servicio de **login** construido con [FastAPI](https://fastapi.tiangolo.com/) que valida las solicitudes con un **JSON Schema** definido manualmente usando la librería [jsonschema](https://python-jsonschema.readthedocs.io/).

## Características
- Validación de entrada usando **JSON Schema Draft 07**.  
- Endpoints documentados automáticamente con **Swagger UI** y **ReDoc**.  
- Manejo de errores claros y personalizados en formato JSON.  
- Simulación de autenticación con email y contraseña.

---

## Requisitos

- Python 3.9+
- FastAPI
- Uvicorn (para ejecutar el servidor)
- jsonschema

Instala las dependencias con:

```bash
pip install fastapi uvicorn jsonschema
