import this

import uvicorn
from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


inventory = {}


@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="the ID of the item you would like to view")):
    return inventory[item_id]


@app.get("/get-by-name")
def get_item(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item name not found")


@app.post("/creat-item/{item_id}")
def creat_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item ID not found")

    inventory[item_id] = item
    return inventory[item_id]


@app.put("/put-item/{item_id}")
def put_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item name not found")

    if item.name is not None:
        inventory[item_id].name = item.name
    if item.price is not None:
        inventory[item_id].price = item.price
    if item.brand is not None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]


@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to be deleted.")):
    if item_id not in inventory:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="item name not found")
    del inventory[item_id]
    return {"deleted": "successfully"}


def main():
    uvicorn.run(app, host="localhost", port=8000)

if __name__ == "__main__":
    main()
