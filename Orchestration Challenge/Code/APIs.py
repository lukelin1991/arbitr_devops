from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel


class TestAPIs:
    def __init__(self) -> None:
        self.users = []
        self.router = APIRouter()
        self.router.add_api_route("/hello", self.hello_world, methods=["GET"])

        self.user_router = APIRouter()
        self.user_router.add_api_route("/add", self.add_user, methods=["POST"])
        self.user_router.add_api_route("/retrieve/{username}", self.retrieve_user, methods=["GET"])
        self.router.include_router(self.user_router, prefix="/user")

    def hello_world(self):
        return "Hello!" 

    class User(BaseModel):
        username: str
        email: str
        full_name: str = None

    def add_user(self, user : User):
        self.users.append(user)
        return {"message" : "Successfully added user!"}
    
    def retrieve_user(self, username : str):
        for user in self.users:
            if username == user.username:
                return {"message" : user}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User: {username}. Does not exist!")
