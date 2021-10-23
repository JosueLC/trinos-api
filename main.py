#Python packages

#Pydantic packages

#FastAPI packages
from fastapi import FastAPI
from fastapi import status

#Local packages
from paths import user, trino

app = FastAPI()

#Path operations to home page
@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Home page",
    tags=["Home"]
    )
def home():
    """
    Home

    This endpoint returns the home page.

    Parameters:
    None

    Returns:
    Dictionary with the message "Working!".
    """
    return {"Trinos API": "Working!"}

#Includes the paths from paths folder
app.include_router(user.router)
app.include_router(trino.router)