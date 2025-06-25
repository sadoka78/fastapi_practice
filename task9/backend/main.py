from fastapi import FastAPI, Depends, HTTPException, status, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Annotated, Optional
from datetime import datetime, timedelta
import uuid

app = FastAPI()

# --- CORS ---
origins = ["http://localhost:3000"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])

# --- Фейковые пользователи с ролями ---
FAKE_USERS_DB = {
    "user": {"username": "user", "password": "password", "role": "user"},
    "admin": {"username": "admin", "password": "adminpass", "role": "admin"},
}

# --- Хранилище активных токенов ---
TOKENS_DB = {}  # Пример: { "token_string": {"username": "user", "created_at": datetime } }

# --- Константа времени жизни токена ---
TOKEN_LIFETIME = timedelta(hours=1)


# --- Pydantic модели ---
class Token(BaseModel):
    access_token: str
    token_type: str
    role: str


# --- Проверка токена и времени жизни ---
async def token_verifier(authorization: Annotated[Optional[str], Header()]):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing Authorization header")

    token = authorization.split(" ")[1]

    if token not in TOKENS_DB:
        raise HTTPException(status_code=401, detail="Invalid token")

    token_data = TOKENS_DB[token]
    created_at = token_data["created_at"]
    if datetime.utcnow() - created_at > TOKEN_LIFETIME:
        del TOKENS_DB[token]
        raise HTTPException(status_code=401, detail="Token expired")

    return token_data


# --- Проверка роли ---
async def admin_required(token_data: Annotated[dict, Depends(token_verifier)]):
    username = token_data["username"]
    user = FAKE_USERS_DB.get(username)
    if not user or user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return token_data


# --- Login ---
@app.post("/api/login", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = FAKE_USERS_DB.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    # Генерируем новый токен
    token = str(uuid.uuid4())
    TOKENS_DB[token] = {"username": user["username"], "created_at": datetime.utcnow()}

    return Token(access_token=token, token_type="bearer", role=user["role"])


# --- Logout ---
@app.post("/api/logout")
async def logout(authorization: Annotated[str, Header()]):
    token = authorization.replace("Bearer ", "")
    if token in TOKENS_DB:
        del TOKENS_DB[token]
    return {"message": "Logged out successfully"}


# --- Защищенный эндпоинт (виден всем авторизованным) ---
@app.get("/api/secret-data")
async def get_secret_data(token_data: Annotated[dict, Depends(token_verifier)]):
    return {"message": f"Hello, {token_data['username']}! This is your secret data."}


# --- Только для админов ---
@app.get("/api/admin-data")
async def get_admin_data(token_data: Annotated[dict, Depends(admin_required)]):
    return {"message": f"Welcome admin {token_data['username']}! This is admin-only data."}
