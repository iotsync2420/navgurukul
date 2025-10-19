from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from routers import users, classes

app = FastAPI(
    title="Live Class Platform 🚀",
    description="A simple yet powerful platform for hosting live video classes",
    version="1.0.0"
)

# ---------------- MIDDLEWARE ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- STATIC + TEMPLATE SETUP ----------------
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ---------------- ROUTERS ----------------
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(classes.router, prefix="/classes", tags=["Classes"])

# ---------------- FRONTEND ROUTES ----------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the main landing page (login or dashboard)."""
    return templates.TemplateResponse("login.html", {"request": request, "title": "Welcome | SwiftWings"})

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    """Render the registration page."""
    return templates.TemplateResponse("register.html", {"request": request, "title": "Register | SwiftWings"})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    """Render the dashboard after login."""
    return templates.TemplateResponse("dashboard.html", {"request": request, "title": "Dashboard | SwiftWings"})

@app.get("/create-class", response_class=HTMLResponse)
async def create_class_page(request: Request):
    """Render the create class page."""
    return templates.TemplateResponse("create_class.html", {"request": request, "title": "Create Class | SwiftWings"})

# ---------------- API ROOT ----------------
@app.get("/api")
def api_root():
    return {"message": "Welcome to SwiftWings Live Class Platform 🚀"}

# ---------------- RUN ----------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("user_login_app:app", host="127.0.0.1", port=8000, reload=True)
