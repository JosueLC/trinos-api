#Python packages

#Pydantic packages

#FastAPI packages
from fastapi import APIRouter
from fastapi import status

#Local packages
from v1 import api_v1

router = APIRouter(
    prefix="/api",
    tags=["API"],
    responses={404:{"description":"Not found"}}
)

#Includes the paths from v1 folder
router.include_router(api_v1.router)