#Python packages
from typing import List
import json

#FastAPI packages
from fastapi import APIRouter
from fastapi import status

#Local packages
from schemas.trino import Trino

router = APIRouter()

DATATRINO_PATH = "../../data/trinos.json"

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
    with open(DATATRINO_PATH, "r", encoding="utf-8") as f:
        trinos = json.load(f)
    return trinos

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
    """
    Post a trino

    This endpoint post a trino.

    Parameters:
    trino: Trino object

    Returns:
    Dictionary with the trino.
    """
    with open("data/trinos.json", "r+", encoding="utf-8") as f:
        trinos = json.load(f)
        trino_dict = trino.dict()
        trino_dict["id"] = str(trino_dict["id"])
        trino_dict["created_at"] = str(trino_dict["created_at"])
        trino_dict["updated_at"] = str(trino_dict["updated_at"])
        trino_dict["by"]["id"] = str(trino_dict["by"]["id"])
        trinos.append(trino_dict)
        f.seek(0)
        json.dump(trinos, f, indent=4)
        f.truncate()
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

