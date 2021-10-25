#Python packages

#Pydantic packages

#FastAPI packages
from fastapi import FastAPI
from fastapi import status

#Local packages
from api import api

app = FastAPI()

#Includes the paths from paths folder
app.include_router(api.router)