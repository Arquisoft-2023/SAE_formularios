from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime
from models.r_preguntas import Respuestas

class Respuesta (BaseModel):
    rdocumento: str
    rapellido: str
    fecharealizacion: str
    rusuarioun: str
    rnombre:str
    respuestas: List[Respuestas]
    