#Python packages
from typing import List

#FastAPI packages
from fastapi import APIRouter
from fastapi import status

#Local packages
from models.trino import Trino

router = APIRouter()

#Path operations to home page
@router.get(
    path="/",
    response_model=List[Trino],
    status_code=status.HTTP_200_OK,
    summary="Get all trinos",
    tags=["Home","Trino"]
    )
def home():
    """
    Home

    This endpoint returns all trinos.

    Parameters:
    None

    Returns:
    Dictionary with the message "Working!".
    """
    return list()

@router.get(
    path="/trino/{trino_id}",
    response_model=Trino,
    status_code=status.HTTP_200_OK,
    summary="Get trino by id",
    tags=["Trino"]
    )
def get_trino(trino_id: int):
    pass

@router.post(
    path="/trino",
    response_model=Trino,
    status_code=status.HTTP_201_CREATED,
    summary="Post a trino",
    tags=["Trino"]
    )
def post_trino(trino: Trino):
    pass

@router.put(
    path="/trino/{trino_id}",
    response_model=Trino,
    status_code=status.HTTP_200_OK,
    summary="Update a trino",
    tags=["Trino"]
    )
def update_trino(trino_id: int, trino: Trino):
    pass

@router.delete(
    path="/trino/{trino_id}",
    response_model=Trino,
    status_code=status.HTTP_200_OK,
    summary="Delete a trino",
    tags=["Trino"]
    )
def delete_trino(trino_id: int):
    pass

