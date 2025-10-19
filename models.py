from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    password: str

class LiveClass(BaseModel):
    title: str
    description: str
    link: str
