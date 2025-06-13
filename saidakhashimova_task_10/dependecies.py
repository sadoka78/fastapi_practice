

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from typing import AsyncGenerator

from models import Base, User
from schemas import UserCreate, UserLogin, UserOut
from utils import get_password_hash, verify_password, verify_token
from datetime import timedelta
from auth import create_access_token, oauth2_scheme
from database import get_db,engine



def require_role(required_role:str):
    async def role_checker(current_user:User=Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permission"
            )
        return current_user
    return role_checker


async def get_current_user(
        token: str=Depends(oauth2_scheme),
        db: AsyncSession = Depends(get_db)

):
    username = verify_token(token)
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=401, detail = 'User not found')
    return user