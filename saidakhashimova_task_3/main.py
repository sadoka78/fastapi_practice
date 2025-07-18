from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from typing import AsyncGenerator

from models import Base, User
from schemas import UserCreate, UserLogin, UserOut
from utils import get_password_hash, verify_password



DATABASE_URL = "postgresql+asyncpg://postgres:saida0512@localhost:5432/notes"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session

# Эндпоинт регистрации
@app.post("/register", response_model=UserOut)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user.username))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_pw=get_password_hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed_pw)

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@app.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user.username))
    db_user = result.scalar_one_or_none()

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return {"message": "Login successful"}
