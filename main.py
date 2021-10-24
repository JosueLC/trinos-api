#Python packages

#Pydantic packages

#FastAPI packages
from fastapi import FastAPI
from fastapi import status

#Local packages
from paths import user, trino

app = FastAPI()

#Includes the paths from paths folder
app.include_router(user.router)
app.include_router(trino.router)