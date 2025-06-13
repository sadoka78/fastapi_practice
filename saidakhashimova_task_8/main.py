from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from database import Base, engine, get_db
from schemas import UserCreate, Token, NoteCreate, Note
import crud, auth
from dependencies import get_current_user
from typing import List

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/register", response_model=Token)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    if await crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await crud.create_user(db, user.email, user.password)
    token = auth.create_access_token(data={"sub": str(new_user.id)})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    token = auth.create_access_token(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/notes", response_model=Note)
async def create_note(note: NoteCreate, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    return await crud.create_note(db, note.text, current_user.id)

@app.get("/notes", response_model=List[Note])
async def read_notes(skip: int = 0, limit: int = 100, search: str = None, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    return await crud.get_user_notes(db, user_id=current_user.id, skip=skip, limit=limit, search=search)
