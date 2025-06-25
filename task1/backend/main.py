import uuid
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# CORS settings
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

# Models
class TodoItem(BaseModel):
    id: str
    task: str
    completed: bool = False

class TodoCreate(BaseModel):
    task: str

class TodoUpdate(BaseModel):
    task: str

# In-memory DB
fake_todo_db: List[TodoItem] = []

# Endpoints

@app.get("/api/todos", response_model=List[TodoItem])
async def get_all_todos():
    return fake_todo_db

@app.post("/api/todos", response_model=TodoItem, status_code=201)
async def create_todo(todo_data: TodoCreate):
    new_todo = TodoItem(
        id=str(uuid.uuid4()),
        task=todo_data.task,
        completed=False
    )
    fake_todo_db.append(new_todo)
    return new_todo

@app.patch("/api/todos/{todo_id}", response_model=TodoItem)
async def toggle_todo_status(todo_id: str):
    for todo in fake_todo_db:
        if todo.id == todo_id:
            todo.completed = not todo.completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/api/todos/{todo_id}", response_model=TodoItem)
async def update_todo(todo_id: str, updated_data: TodoUpdate):
    for todo in fake_todo_db:
        if todo.id == todo_id:
            todo.task = updated_data.task
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")




@app.delete("/api/todos/{todo_id}", status_code=204)
async def delete_todo(todo_id: str):
    todo_to_delete = next((todo for todo in fake_todo_db if todo.id == todo_id), None)
    if not todo_to_delete:
        raise HTTPException(status_code=404, detail="Todo not found")
    fake_todo_db.remove(todo_to_delete)
    return
@app.delete("/api/todos/completed")
async def delete_completed_todos():
    global fake_todo_db
    before_count = len(fake_todo_db)
    fake_todo_db = [todo for todo in fake_todo_db if not todo.completed]
    after_count = len(fake_todo_db)
    deleted_count = before_count - after_count
    return {"message": f"Deleted {deleted_count} completed todos"}

@app.get("/")
async def root():
    return {"message": "FastAPI To-Do Backend is running!"}
