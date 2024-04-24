from fastapi import APIRouter

todo_router = APIRouter()

todo_list = []

# curl -X POST http://localhost:8000/todo -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\": 1, \"item\":\"First Todo is to finish this book! \"}"
@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
  todo_list.append(todo)
  return {
    "message": "Todo added successfully."
  }

# curl -X GET http://localhost:8000/todo -H "accept: application/json"
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
  return {
    "todos": todo_list
  }