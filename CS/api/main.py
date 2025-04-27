from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# 가격표
price_table = {
    "apple": 3.5,
    "banana": 2.0,
    "orange": 4.0
}

class Item(BaseModel):
    name: str

@app.post("/get-price/")
def get_price(item: Item):
    price = price_table.get(item.name.lower())
    if price is not None:
        return {"name": item.name, "price": price}
    else:
        return {"error": "Item not found"}
    
@app.get("/items/", response_model=Dict[str, float])
def get_all_items():
    return price_table

# 서버 띄우기 (기본: 로컬)
# python3 -m uvicorn main:app --reload