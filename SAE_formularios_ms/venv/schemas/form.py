from models.respuesta import Respuesta
from models.preguntas_respuestas import Preguntasrespuestas 
from typing import List
def entidad_formulario(item) -> dict:
    return{
        "idform": str(item["_id"]),
        "documento": item ["documento"],
        "nombre": item ["nombre"],
        "apellido": item ["apellido"],
        "usuarioun": item ["usuarioun"],
        "fechacreacion": item ["fechacreacion"],
        "tipologia": item ["tipologia"],
        "respuestas": List[Respuesta],
        "preguntasrespuestas": List[Preguntasrespuestas]

    }

def entidad_formularios(entity) -> list:
    return[item for item in entity]