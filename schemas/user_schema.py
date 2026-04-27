from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int
    name: str
    email: EmailStr

from pydantic import BaseModel


class ErrorSchema(BaseModel):
    detail: str
