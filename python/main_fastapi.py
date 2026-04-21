from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

app = FastAPI()

users = []
current_id = 1
VALID_TOKEN = "Bearer testtoken123"


class UserCreate(BaseModel):
    name: str
    email: EmailStr

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        return value


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if value is not None and not value.strip():
            raise ValueError("Name cannot be empty")
        return value


def check_auth(authorization: Optional[str]):
    if authorization != VALID_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    global current_id

    for existing_user in users:
        if existing_user["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email already exists")

    new_user = {
        "id": current_id,
        "name": user.name,
        "email": user.email
    }
    users.append(new_user)
    current_id += 1
    return new_user


@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int, authorization: Optional[str] = Header(default=None)):
    check_auth(authorization)

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(status_code=404, detail="User not found")


@app.patch("/users/{user_id}")
def update_user(
    user_id: int,
    updated_data: UserUpdate,
    authorization: Optional[str] = Header(default=None)
):
    check_auth(authorization)

    for user in users:
        if user["id"] == user_id:
            if updated_data.name is not None:
                user["name"] = updated_data.name
            if updated_data.email is not None:
                for existing_user in users:
                    if existing_user["email"] == updated_data.email and existing_user["id"] != user_id:
                        raise HTTPException(status_code=400, detail="Email already exists")
                user["email"] = updated_data.email
            return user

    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return {"message": "User deleted"}

    raise HTTPException(status_code=404, detail="User not found")