from fastapi import FastAPI
from routes.formularios import form

app = FastAPI()

app.include_router(form)