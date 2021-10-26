#Python packages

#Pydantic packages

#FastAPI packages
from fastapi import APIRouter
from fastapi import status

#Local packages
from .paths import user, trino

router = APIRouter(
    prefix="/v1",
    tags=["API","version 1"],
    responses={404:{"description":"Not found"}}
)

#Includes the paths from paths folder
router.include_router(user.router)
router.include_router(trino.router)