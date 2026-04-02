from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items: List[Item] = [
    Item(id=1, name="Notebook", description="A reusable note-taking app."),
    Item(id=2, name="Pen", description="A smooth-writing pen."),
]

@app.get("/items", response_model=List[Item])
def list_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    items.append(item)
    return item
