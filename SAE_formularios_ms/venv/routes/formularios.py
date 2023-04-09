from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.form import entidad_formulario, entidad_formularios
from models.Formulario import Form
from bson import ObjectId
from typing import List
from models.formulario_r import Form_r
from starlette.status import HTTP_204_NO_CONTENT




form = APIRouter()


@form.get('/formularios/', response_model=list[Form])
def buscar_formularios():
    return entidad_formularios(conn.local.formularios.find())


@form.post('/formularios/crear/', response_model= Form)
def crear_formulario(formulario: Form):
    formulario_dict = formulario.dict()
    nuevo_formulario = dict(formulario_dict)
    id = conn.local.formularios.insert_one(nuevo_formulario).inserted_id
    formulario = conn.local.formularios.find_one({"_id": id})
    return formulario


@form.get('/tamizajes/{id}')
def reportar_tamisajes(id:str):
    formulario= Form.parse_obj(conn.local.formularios.find_one({"_id": ObjectId(id)}))
    return formulario.respuestas

@form.get('/tamizajes/estudiante/{id}/{usuario_un}')
def reportar_tamisajes_estudiante(id:str, usuario_un:str):
    formulario= Form_r.parse_obj(conn.local.formularios.find_one({"_id": ObjectId(id)}))
    tamizaje = next((o for o in formulario.respuestas if o.rusuarioun == usuario_un), None)
    return tamizaje
    

@form.put('/tamizajes/bienestar/{id}')
def realizar_tamizaje(id:str, formulario: Form_r):
    formulario_dict = formulario.dict()
    nuevo_formulario = dict(formulario_dict)
    conn.local.formularios.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": nuevo_formulario})
    
    return Response(status_code=HTTP_204_NO_CONTENT)



@form.get('/formularios/id/{id}', response_model= Form)
def buscar_formulario(id: str):
     return conn.local.formularios.find_one({"_id": ObjectId(id)})


@form.put('/forms/actua/{id}')
def actualizar_formulario(id: str, formulario: Form):
    formulario_dict = formulario.dict()
    nuevo_formulario = dict(formulario_dict)
    conn.local.formularios.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": nuevo_formulario})
    return nuevo_formulario
    


@form.delete('/forms/borrar/{id}', status_code=status.HTTP_204_NO_CONTENT)
def borrar_formulario(id: str):
    entidad_formulario(
        conn.local.formularios.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
