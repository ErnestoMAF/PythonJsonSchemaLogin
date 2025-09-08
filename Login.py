from fastapi import FastAPI, Request, HTTPException, status
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json

app = FastAPI(
    title="API de Autenticación (Validación Manual)",
    description="Un servicio de login que valida las solicitudes con un JSON Schema definido manualmente.",
    version="1.0.0",
)


LOGIN_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "email": {
            "type": "string",
            "format": "email",
            "description": "El correo electrónico del usuario."
        },
        "password": {
            "type": "string",
            "minLength": 8,
            "description": "La contraseña debe tener al menos 8 caracteres."
        }
    },
    "required": ["email", "password"],
    "additionalProperties": False # No permite propiedades adicionales en el JSON
}


@app.post("/login-manual", tags=["Autenticación"])
async def login_manual(request: Request):
    """
    Valida las credenciales del usuario usando una declaración explícita de JSON Schema.
    """
    # Obtenemos el cuerpo (body) de la solicitud como un JSON
    try:
        body = await request.json()
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El cuerpo de la solicitud no es un JSON válido."
        )

    # Validamos el JSON contra nuestro esquema
    try:
        validate(instance=body, schema=LOGIN_SCHEMA)
    except ValidationError as e:
        # Si la validación falla, capturamos el error y devolvemos una respuesta clara.
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f"Error de validación del JSON: {e.message}"
        )

    # --- Lógica de autenticación (si la validación fue exitosa) ---
    email = body.get("email")
    password = body.get("password")

    # Simulación de un usuario y contraseña correctos
    if email == "usuario@ejemplo.com" and password == "unacontraseñasegura":
        return {"message": f"¡Bienvenido (manual), {email}!", "token": "aqui_iria_un_token_jwt_simulado"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo electrónico o contraseña incorrectos",
        )