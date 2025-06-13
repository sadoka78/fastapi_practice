from pydantic import BaseModel
from datetime import datetime
class UserCreate(BaseModel):
    username:str
    password:str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id:int
    username:str

    class Config:
        from_attributes = True

class NoteBase(BaseModel):
    text:str

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class NoteOut(NoteBase):
    id:int
    created_at:datetime

    class Config:
        orm_mode = True


