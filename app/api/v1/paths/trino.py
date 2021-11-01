#Python packages
from datetime import datetime
from typing import List, Dict
import json

#FastAPI packages
from fastapi import APIRouter
from fastapi import status, HTTPException
from fastapi import Body, Query

#Local packages
from ..schemas.trino import Trino
from ...data.data_storage_service import DataStorageService

router = APIRouter()

dss = DataStorageService("trinos")
users = DataStorageService("users").get_data_storage_dictionary_elements(["id"])

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
    A json object with all trinos with this structure:
    
        - id: UUID
        - content: String
        - created_at: DateTime
        - updated_at: DateTime
        - by: UserBase (id, username, email)
    """
    trinos = dss.get_data_storage_dictionary_as_list()
    return trinos

@router.get(
    path="/trino/{trino_id}",
    response_model=Trino,
    status_code=status.HTTP_200_OK,
    summary="Get trino by id",
    tags=["Trino"]
    )
def get_trino(
    trino_id: str = Query(..., description="Trino id")
    ):
    return dss.get_data_storage_dictionary_element(trino_id)

@router.post(
    path="/trino",
    response_model=Trino,
    status_code=status.HTTP_201_CREATED,
    summary="Post a trino",
    tags=["Trino"]
    )
def post_trino(
    trino: Trino = Body(...)
):
    """
    Post a trino

    This endpoint post a trino.

    Parameters:
    trino: Trino object

    Returns:
    Dictionary with the trino.
    """
    #Check if the user exists
    user_id = {"id": str(trino.by.id)}
    if user_id not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
        )
    trino_dict = trino.dict()
    trino_dict["id"] = dss.generate_id()
    trino_dict["created_at"] = str(trino_dict["created_at"])
    trino_dict["updated_at"] = str(trino_dict["updated_at"])
    trino_dict["by"]["id"] = str(trino_dict["by"]["id"])
    if dss.add_data_storage_dictionary_element(trino_dict["id"],trino_dict):
        return trino_dict
    else:
        if dss.status == 4:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failure saving a trino"
            )
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
            detail="Trino ID already exists"
            )

@router.put(
    path="/trino/{trino_id}",
    response_model=Trino,
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Trino"]
    )
def update_trino(
    trino_id: str = Query(...),
    trino: Trino = Body(...)
):
    """
    Update a trino

    This endpoint update a trino.

    Parameters:
    trino_id: UUID of the trino
    trino: Trino object

    Returns:
    Dictionary with the trino.
    """
    #Get original trino
    original_trino = dss.get_data_storage_dictionary_element(trino_id)
    if original_trino is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trino not found"
        )
    #Update trino
    original_trino["content"] = trino.content
    original_trino["updated_at"] = str(datetime.now())
    if dss.set_data_storage_dictionary_element(trino_id,original_trino):
        return Trino(**original_trino)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error updating trino"
        )


@router.delete(
    path="/trino/{trino_id}",
    response_model=Trino,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Delete a trino",
    tags=["Trino"]
    )
def delete_trino(
    trino_id: str = Query(...),
):
    """
    Delete a trino

    This endpoint delete a trino.

    Parameters:
    trino_id: UUID of the trino

    Returns:
    Dictionary with the trino.
    """
    #Get original trino
    original_trino = dss.get_data_storage_dictionary_element(trino_id)
    if original_trino is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Trino not found"
        )
    if dss.delete_data_storage_dictionary_element(trino_id):
        return Trino(**original_trino)
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error deleting trino"
        )

