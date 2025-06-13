from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import User, Note
from auth import get_password_hash, verify_password

async def create_user(db: AsyncSession, email: str, password: str):
    user = User(email=email, hashed_password=get_password_hash(password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()

async def authenticate_user(db: AsyncSession, email: str, password: str):
    user = await get_user_by_email(db, email)
    if user and verify_password(password, user.hashed_password):
        return user
    return None

async def create_note(db: AsyncSession, text: str, user_id: int):
    note = Note(text=text, owner_id=user_id)
    db.add(note)
    await db.commit()
    await db.refresh(note)
    return note

async def get_user_notes(db: AsyncSession, user_id: int, skip: int = 0, limit: int = 100, search: str = None):
    stmt = select(Note).where(Note.owner_id == user_id)
    if search:
        stmt = stmt.where(Note.text.ilike(f"%{search}%"))
    stmt = stmt.offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()
