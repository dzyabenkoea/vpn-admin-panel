from fastapi import FastAPI
from typing import Union
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from src.db.models.users import User
from src.db.db import connect


app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
def get_users(request: Request):
    users = []
    with connect() as conn:
        users = conn.query(User).all()
    return templates.TemplateResponse(request=request, name="users/list.j2", context={"users": users})

@app.post("/users/add")
def get_users(request: Request):
    
    data = request.json()
    
    with connect() as conn:
        users = conn.query(User).all()
        
    return templates.TemplateResponse(request=request, name="users/list.j2", context={"users": users})