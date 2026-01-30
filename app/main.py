# app/main.py
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from . import models, database, utils

# 1. Инициализация БД (создает таблицы при запуске)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Redline Server")

# 2. Подключение папок
# Если у тебя будут отдельные CSS/JS файлы, они пойдут в static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Шаблоны (твои HTML файлы)
templates = Jinja2Templates(directory="templates")

# --- МАРШРУТЫ (ROUTES) ---

@app.get("/")
async def read_root(request: Request):
    """Отображает главную страницу"""
    # Мы можем передать данные сразу при загрузке, но лучше подгружать JS-ом
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/status")
async def get_server_status():
    """API для получения онлайна (вызывается из JS)"""
    status = await utils.get_minecraft_status()
    return status

# Пример работы с БД (на будущее)
@app.post("/api/players/")
def create_player(username: str, db: Session = Depends(database.get_db)):
    # Здесь будет логика добавления игрока
    return {"msg": f"Player {username} checked"}