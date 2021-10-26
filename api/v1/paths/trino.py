#Python packages
from typing import List, Dict
import json

#FastAPI packages
from fastapi import APIRouter
from fastapi import status

#Local packages
from ..schemas.trino import Trino
from ...data.data_storage_service import DataStorageService

router = APIRouter()

dss = DataStorageService("trinos")

#Path operations to home page
@router.get(
    path="/",
    response_model=Dict[str,Trino],
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
    A json object with all trinos with this structure:
    
        - id: UUID
        - content: String
        - created_at: DateTime
        - updated_at: DateTime
        - by: UserBase (id, username, email)
    """
    trinos = dss.data_storage_dictionary
    return trinos

@router.get(
    path="/trino/{trino_id}",
    response_model=Trino,
    status_code=status.HTTP_200_OK,
    summary="Get trino by id",
    tags=["Trino"]
    )
def get_trino(trino_id: int):
    return dss.get_data_storage_dictionary_element(trino_id)

@router.post(
    path="/trino",
    response_model=Trino,
    status_code=status.HTTP_201_CREATED,
    summary="Post a trino",
    tags=["Trino"]
    )
def post_trino(trino: Trino):
    """
    Post a trino

    This endpoint post a trino.

    Parameters:
    trino: Trino object

    Returns:
    Dictionary with the trino.
    """

    trino_dict = trino.dict()
    trino_dict["id"] = str(trino_dict["id"])
    trino_dict["created_at"] = str(trino_dict["created_at"])
    trino_dict["updated_at"] = str(trino_dict["updated_at"])
    trino_dict["by"]["id"] = str(trino_dict["by"]["id"])
    dss.add_data_storage_dictionary_element(str(trino.id),trino_dict)
    return trino

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

