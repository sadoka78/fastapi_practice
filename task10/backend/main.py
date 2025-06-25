import json
import uuid
from datetime import datetime, timezone
from fastapi import FastAPI, Depends, HTTPException, status, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Annotated, Optional
import aiofiles

app = FastAPI()

# --- CORS ---
origins = ["http://localhost:3000"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

# --- Файлы ---
POSTS_FILE = "data/posts.json"
LIKES_FILE = "data/likes.json"

# --- Фейковые пользователи ---
FAKE_USERS_DB = {
    "user1": {"id": "1", "username": "user1", "password": "password1"},
    "user2": {"id": "2", "username": "user2", "password": "password2"},
}

# --- Pydantic модели ---
class Post(BaseModel):
    id: str
    text: str
    timestamp: datetime
    owner_id: str
    owner_username: str
    likes: List[str] = []

class PostCreate(BaseModel):
    text: str

class User(BaseModel):
    id: str
    username: str

# --- Файловые операции ---
async def read_posts() -> List[Post]:
    try:
        async with aiofiles.open(POSTS_FILE, mode='r', encoding='utf-8') as f:
            content = await f.read()
            return [Post(**item) for item in json.loads(content)] if content else []
    except FileNotFoundError:
        return []

async def write_posts(posts: List[Post]):
    export_data = [post.model_dump(mode='json') for post in posts]
    async with aiofiles.open(POSTS_FILE, mode='w', encoding='utf-8') as f:
        await f.write(json.dumps(export_data, indent=4, ensure_ascii=False))

async def read_likes() -> Dict[str, List[str]]:
    try:
        async with aiofiles.open(LIKES_FILE, mode='r', encoding='utf-8') as f:
            content = await f.read()
            return json.loads(content) if content else {}
    except FileNotFoundError:
        return {}

async def write_likes(likes: Dict[str, List[str]]):
    async with aiofiles.open(LIKES_FILE, mode='w', encoding='utf-8') as f:
        await f.write(json.dumps(likes, indent=4, ensure_ascii=False))

# --- Аутентификация ---
async def get_current_user(authorization: Annotated[Optional[str], Header()]) -> User:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid or missing Authorization header")

    token = authorization.replace("Bearer ", "")
    user_data = FAKE_USERS_DB.get(token)

    if not user_data:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid token")
    return User(id=user_data["id"], username=user_data["username"])

@app.post("/api/login")
async def login(form_data: Dict[str, str]):
    username = form_data.get("username")
    password = form_data.get("password")
    user = FAKE_USERS_DB.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Incorrect username or password")
    return {
        "access_token": user["username"],  # Токен — просто username
        "token_type": "bearer",
        "user": {"id": user["id"], "username": user["username"]}
    }

# --- Посты ---
@app.get("/api/posts", response_model=List[Post])
async def list_posts():
    posts = await read_posts()
    likes = await read_likes()

    # Проставляем список лайков в каждый пост
    for post in posts:
        post.likes = likes.get(post.id, [])

    return sorted(posts, key=lambda p: p.timestamp, reverse=True)

@app.post("/api/posts", response_model=Post, status_code=201)
async def create_post(post_data: PostCreate, current_user: Annotated[User, Depends(get_current_user)]):
    posts = await read_posts()
    new_post = Post(
        id=str(uuid.uuid4()),
        text=post_data.text,
        timestamp=datetime.now(timezone.utc),
        owner_id=current_user.id,
        owner_username=current_user.username
    )
    posts.append(new_post)
    await write_posts(posts)
    return new_post

@app.delete("/api/posts/{post_id}", status_code=204)
async def delete_post(post_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    posts = await read_posts()
    post_to_delete = next((p for p in posts if p.id == post_id), None)

    if not post_to_delete:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Post not found")

    if post_to_delete.owner_id != current_user.id:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "You cannot delete this post")

    posts.remove(post_to_delete)
    await write_posts(posts)

# --- Лайки ---
@app.post("/api/posts/{post_id}/like")
async def like_post(post_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    likes = await read_likes()
    user_id = current_user.id
    if post_id not in likes:
        likes[post_id] = []
    if user_id not in likes[post_id]:
        likes[post_id].append(user_id)
        await write_likes(likes)
    return {"message": "Liked"}

@app.delete("/api/posts/{post_id}/like")
async def unlike_post(post_id: str, current_user: Annotated[User, Depends(get_current_user)]):
    likes = await read_likes()
    user_id = current_user.id
    if post_id in likes and user_id in likes[post_id]:
        likes[post_id].remove(user_id)
        await write_likes(likes)
    return {"message": "Unliked"}

@app.get("/api/likes")
async def get_all_likes():
    return await read_likes()

# --- Посты конкретного пользователя (Профиль) ---
@app.get("/api/users/{username}/posts", response_model=List[Post])
async def get_user_posts(username: str):
    posts = await read_posts()
    user_posts = [post for post in posts if post.owner_username == username]
    return sorted(user_posts, key=lambda p: p.timestamp, reverse=True)
