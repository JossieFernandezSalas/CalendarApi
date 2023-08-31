# Author: Jossie Esteban Fernández Salas
# Email: jossie.fernandez.salas@gmail.com
# Linkedin: linkedin.com/in/jossiefernandez

from fastapi.responses import JSONResponse


def response_json(message: str, status: int = 200) -> JSONResponse:
    return JSONResponse(content={"message": message}, status_code=status)


