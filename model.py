from typing import Optional
from pydantic import BaseModel
from fastapi import Form
  
class Todo(BaseModel):
  id: Optional[int]
  item: str

  @classmethod
  def as_form(cls, item: str = Form(...)):
    return cls(item=item)

  model_config = {
    "json_schema_extra" : {
      "example": {
        "id": 1,
        "item": "this is example schema"
      }
    }
  }

class TodoItem(BaseModel):
  item: str

  model_config = {
    "json_schema_extra" : {
      "example" : {
        "item" : "example item"
      }
    }
  }

class TodoItems(BaseModel):
  todos: list[TodoItem]

  model_config = {
    "json_schema_extra" : {
      "example" : {
        "todos" : [
          {
            "item" : "example 1"
          }, 
          {
            "item" : "example 2"
          }
        ]
      }
    }
  }