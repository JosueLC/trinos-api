#Python packages
from typing import List

#FastAPI packages
from fastapi import APIRouter
from fastapi import status
from fastapi import Body

#Local packages
from models.user import User, UserFull

router = APIRouter()

@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Sign up a new user",
    tags=["User"]
)
def signup():
    """
    Sign up a new user

    This endpoint will create a new user.

    Parameters
    - Request body parameters:
        - user: UserFull object

    Returns
    A json object with the user's information:
        - id: User's id (UUID)
        - username: User's username (str)
        - email: User's email (EmailStr)
        - first_name: User's first name (str)
        - last_name: User's last name (str)
        - birth_date: User's birth date (date)'

    """
    return user

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
