from pydantic import BaseModel
  
class Todo(BaseModel):
  id: int
  item: str

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