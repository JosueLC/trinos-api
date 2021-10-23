#Python packages
from typing import List

#FastAPI packages
from fastapi import APIRouter
from fastapi import status

#Local packages
from models.user import User

router = APIRouter()

@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Sign up a new user",
    tags=["User"]
)
async def signup(user: User):
    pass

@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["User"]
)
async def login(user: User):
    pass

@router.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Get all users",
    tags=["User"]
)
async def get_users():
    pass

@router.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Get a user",
    tags=["User"]
)
async def get_user(user_id: int):
    pass

@router.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["User"]
)
async def update_user(user_id: int, user: User):
    pass

@router.delete(
    path="/users/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["User"]
)
async def delete_user(user_id: int):
    pass
