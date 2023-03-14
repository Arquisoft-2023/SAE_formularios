from pydantic import BaseModel,parse_file_as
from typing import Optional, List
from pydantic import ValidationError
# min 6 video of pydantic
from datetime import date, datetime
from models.respuesta import Respuesta
from models.preguntas_respuestas import Preguntasrespuestas
import json



class Form(BaseModel):
    documento: Optional[str] = "digite su documento"
    nombre :Optional[str] = "digite su nombre"
    apellido: Optional[str] = "digite su apellido"
    usuarioun:Optional[str] = "digite su usuario unal"
    fechacreacion: str
    idform: Optional[str]
    tipologia: str =  "indique la tipologia del formulario"
    respuestas: Optional[List[Respuesta]]=[]
    preguntasrespuestas: List[Preguntasrespuestas]
  
