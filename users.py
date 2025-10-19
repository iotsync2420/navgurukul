from fastapi import APIRouter, HTTPException, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from utils.jwt_handler import create_access_token
from utils.database import users_db
import hashlib

router = APIRouter()
templates = Jinja2Templates(directory="templates")

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
async def register_user(request: Request, name: str = Form(...), email: str = Form(...), password: str = Form(...)):
    if email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[email] = {"name": name, "password": hash_password(password)}
    return RedirectResponse("/users/login", status_code=303)

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login_user(request: Request, email: str = Form(...), password: str = Form(...)):
    user = users_db.get(email)
    if not user or user["password"] != hash_password(password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": email})
    response = RedirectResponse("/users/profile", status_code=303)
    response.set_cookie("access_token", token)
    return response

@router.get("/profile", response_class=HTMLResponse)
async def profile_page(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})
