from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
security = HTTPBearer()

registered_users = {}
tokens = {}
users = []
current_id = 1


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

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

def check_auth(authorization: Optional[str]):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")

    token = authorization.replace("Bearer ", "")
    user = tokens.get(token)

    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return user

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

@app.post("/register", status_code=201)
def register_user(payload: RegisterRequest):
    if payload.email in registered_users:
        raise HTTPException(status_code=409, detail="User with this email already exists")

    user_id = len(registered_users) + 1

    registered_users[payload.email] = {
        "id": user_id,
        "name": payload.name,
        "email": payload.email,
        "password": payload.password
    }

    return {
        "id": user_id,
        "name": payload.name,
        "email": payload.email
    }


@app.post("/login")
def login_user(payload: LoginRequest):
    user = registered_users.get(payload.email)

    if not user or user["password"] != payload.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = f"token-{user['id']}"
    tokens[token] = user

    return {"access_token": token, "token_type": "bearer"}


@app.get("/profile")
def get_profile(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    user = tokens.get(token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"]
    }