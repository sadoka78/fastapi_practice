from passlib.context import CryptContext
from config import SECRET_KEY ,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import  HTTPException, status
from datetime import datetime
from jose import JWTError,jwt

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_password_hash(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)

def verify_token(token:str)->str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM] )
        username:str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception