import secrets
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl
from typing import Optional

app = FastAPI()

# --- Настройка CORS ---
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- "База данных" ---
# Пример структуры:
# {
#   "abc123": {
#       "long_url": "https://example.com",
#       "clicks": 0,
#       "created_at": datetime
#   }
# }
url_db = {}

# --- Pydantic модель ---
class URLCreate(BaseModel):
    long_url: HttpUrl
    custom_code: Optional[str] = None  # Кастомный код, опционально

# --- Конфигурация срока действия (например, 7 дней) ---
EXPIRY_DAYS = 7

# --- Создание короткой ссылки ---
@app.post("/api/shorten")
def create_short_url(url_data: URLCreate, request: Request):
    long_url = str(url_data.long_url)

    # Если пользователь указал свой кастомный код
    if url_data.custom_code:
        short_code = url_data.custom_code
        if short_code in url_db:
            raise HTTPException(status_code=400, detail="Код уже занят")
    else:
        # Генерация случайного кода
        short_code = secrets.token_urlsafe(4)
        while short_code in url_db:
            short_code = secrets.token_urlsafe(4)

    # Сохраняем в "базу"
    url_db[short_code] = {
        "long_url": long_url,
        "clicks": 0,
        "created_at": datetime.utcnow()
    }

    base_url = str(request.base_url)
    short_url = f"{base_url}{short_code}"

    return {"short_url": short_url, "clicks": 0}

# --- Редирект и подсчёт кликов ---
@app.get("/{short_code}")
def redirect_to_long_url(short_code: str):
    url_data = url_db.get(short_code)

    if not url_data:
        raise HTTPException(status_code=404, detail="Short URL not found")

    # Проверяем срок действия
    created_at = url_data["created_at"]
    expiry_date = created_at + timedelta(days=EXPIRY_DAYS)
    if datetime.utcnow() > expiry_date:
        raise HTTPException(status_code=404, detail="This link has expired")

    # Увеличиваем счетчик
    url_data["clicks"] += 1

    return RedirectResponse(url=url_data["long_url"])

# --- Получить количество кликов (опциональный GET-эндпоинт для фронта) ---
@app.get("/api/clicks/{short_code}")
def get_clicks(short_code: str):
    url_data = url_db.get(short_code)
    if not url_data:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return {"clicks": url_data["clicks"]}
