from pydantic import BaseModel
from models.posibles_respuestas import Posiblesrespuestas
from typing import  List

class Preguntasrespuestas (BaseModel):
    pregunta: str
    posiblesrespuestas: List[Posiblesrespuestas]