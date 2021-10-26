#Python packages
from typing import List
import json

#FastAPI packages
from fastapi import APIRouter
from fastapi import status, HTTPException
from fastapi import Body
from fastapi.param_functions import Query

#Local packages
from ..schemas.user import User, UserFull

router = APIRouter()

DATAUSER_PATH = "../../data/users.json"

@router.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Sign up a new user",
    tags=["User"]
)
def signup(
    user: UserFull = Body(
        ...,
    )
):
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
    with open(DATAUSER_PATH, "r+", encoding="utf-8") as f:
        users = json.load(f)
        user_dict = user.dict()
        user_dict["id"] = str(user_dict["id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        users.append(user_dict)
        f.seek(0)
        json.dump(users, f, indent=4)
        f.truncate()
    return user

@router.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["User"]
)
def login(
    username:str = Body(
        ...,
        min_length=2,
        ),
    password:str = Body(
        ...,
        min_length=8,
        )
):
    """
    Login

    Check that user exists in database

    Parameters:
    -Body Parameters:

        - username: str = user's nickname.
        - password: str = user's password.

    Returns:

        - User object if user is found and password matches.
        - HTTP Error 401 if user is found but password does not match.
        - HTTP Error 404 if user is not found.
    """
    with open(DATAUSER_PATH,"r",encoding="utf-8") as f:
        users = json.load(f)
        for user in users:
            if user["username"] == username:
                if user["password"] == password:
                    response = User(**user)
                    return response
                else:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid password."
                    )
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )
    

@router.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Get all users",
    tags=["User"]
)
def get_users():
    """
    Get all users

    This endpoint will return a list of all users.

    Returns
    A json object with the all users' information:
        - id: User's id (UUID)
        - username: User's username (str)
        - email: User's email (EmailStr)
        - first_name: User's first name (str)
        - last_name: User's last name (str)
        - birth_date: User's birth date (date)'

    """
    with open(DATAUSER_PATH, "r", encoding="utf-8") as f:
        users = json.load(f)
    return users

@router.get(
    path="/users/{username}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Get a user",
    tags=["User"]
)
def get_user(
    username: str = Query(
        ...,
        min_length=2,
        )
    ):
    """
    Get a user

    This endpoint will return the user required.

    Parameters:
    Query parameters:

    - username: str = User nickname.

    Returns
    A json object with the user's information:

        - id: User's id (UUID)
        - username: User's username (str)
        - email: User's email (EmailStr)
        - first_name: User's first name (str)
        - last_name: User's last name (str)
        - birth_date: User's birth date (date)'

    """
    with open(DATAUSER_PATH,"r",encoding="utf-8") as f:
        users = json.load(f)
        for user in users:
            if user["username"] == username:
                response = User(**user)
                return response
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )

@router.put(
    path="/users/{username}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["User"]
)
def update_user(
    username: str = Query(
        ...,
        min_length=2,
        ),
    user_updated: UserFull = Body(...)
    ):
    """
    Update a user

    This endpoint will update the user required.

    Parameters:
    Query parameters:

    - username: str = User nickname.

    Body parameters:

    - user_updated: UserFull = Information about the user to be update.

    Returns
    A json object with the user's information:

        - id: User's id (UUID)
        - username: User's username (str)
        - email: User's email (EmailStr)
        - first_name: User's first name (str)
        - last_name: User's last name (str)
        - birth_date: User's birth date (date)'

    """
    with open(DATAUSER_PATH, "r+", encoding="utf-8") as f:
        users = json.load(f)
        for user in users:
            if user["username"] == username:
                user_dict = user_updated.dict()
                user_dict["id"] = str(user_dict["id"])
                user_dict["birth_date"] = str(user_dict["birth_date"])
                users[users.index(user)] = user_dict
                f.seek(0)
                json.dump(users, f, indent=4)
                f.truncate()
                return user_dict
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )

@router.delete(
    path="/users/{username}",
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["User"]
)
def delete_user(
    username: str = Query(
        ...,
        min_length=2,
        )
    ):
    """
    Delete a user

    This endpoint will delete the user required.

    Parameters:
    Query parameters:

    - username: str = User nickname.

    Returns
    A dictionary with the following keys:
    {"user": username, "status":"deleted"}
    """
    with open(DATAUSER_PATH, "r+", encoding="utf-8") as f:
        users = json.load(f)
        for user in users:
            if user["username"] == username:
                del users[users.index(user)]
                f.seek(0)
                json.dump(users, f, indent=4)
                f.truncate()
                return {"username":user["username"], "status":"deleted"}
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "User not found"
        )