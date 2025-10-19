from pydantic import BaseModel, EmailStr
from typing import Optional, List

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    class Config:
        orm_mode = True


class ClassCreate(BaseModel):
    title: str
    description: Optional[str] = None

class ClassOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    link: str
    room: str
    class Config:
        orm_mode = True

