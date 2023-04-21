from fastapi import FastAPI
from routes.formularios import form
from dotenv import load_dotenv
from pathlib import Path
import os


app = FastAPI()

app.include_router(form)

from dotenv import load_dotenv
from pathlib import Path
import os
load_dotenv()


HOST = str( os.environ['DATABASE_HOST'])
PORT = str(os.environ['DATABASE_PORT'])
link = "mongodb://" + HOST + ":" + PORT+"/"
print(link)
