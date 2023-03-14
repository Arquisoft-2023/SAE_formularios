from pydantic import BaseModel

class Respuestas (BaseModel):
    respuesta: str
    nivelriesgo: str