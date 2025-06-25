from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Модели ---
class PostBase(BaseModel):
    slug: str
    title: str
    author: str
    date: str
    category: str

class PostFull(PostBase):
    content: str

# --- "База данных" ---
fake_posts_db: List[PostFull] = [
    PostFull(
        slug="first-post",
        title="Мой первый пост",
        content="# Введение\nЭто содержимое первого поста в Markdown формате.",
        author="Алексей",
        date="2025-06-25",
        category="Общее"
    ),
    PostFull(
        slug="fastapi-and-nextjs",
        title="FastAPI + Next.js = ❤️",
        content="## Почему это круто\nFastAPI и Next.js — отличный стек для современных веб-приложений.",
        author="Мария",
        date="2025-06-24",
        category="Технологии"
    ),
    PostFull(
        slug="why-i-love-python",
        title="Почему я люблю Python",
        content="### Простота и мощь\nPython — простой и мощный язык для всех задач.",
        author="Иван",
        date="2025-06-23",
        category="Программирование"
    )
]

# --- Эндпоинты ---
@app.get("/api/posts", response_model=List[PostBase])
async def get_all_posts():
    return fake_posts_db

@app.get("/api/posts/{slug}", response_model=PostFull)
async def get_post_by_slug(slug: str):
    for post in fake_posts_db:
        if post.slug == slug:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.get("/")
async def root():
    return {"message": "Blog API is running"}
