#Python packages

#Pydantic packages

#FastAPI packages
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

#Path operations to home page
@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    summary="Home page",
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
