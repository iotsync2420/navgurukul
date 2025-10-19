from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uuid

router = APIRouter()
templates = Jinja2Templates(directory="templates")

classes_db = {}

@router.get("/create", response_class=HTMLResponse)
async def create_class_page(request: Request):
    return templates.TemplateResponse("create_class.html", {"request": request})

@router.post("/create", response_class=HTMLResponse)
async def create_class(request: Request, title: str = Form(...), description: str = Form(...)):
    class_id = str(uuid.uuid4())[:8]
    link = f"http://127.0.0.1:8000/classes/live/{class_id}"
    classes_db[class_id] = {"title": title, "description": description, "link": link}
    return templates.TemplateResponse("class_created.html", {"request": request, "link": link})

@router.get("/live/{class_id}", response_class=HTMLResponse)
async def live_class(request: Request, class_id: str):
    class_info = classes_db.get(class_id)
    return templates.TemplateResponse("live_class.html", {"request": request, "class_info": class_info})
