from csv import DictReader
from typing import Dict, List, Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/cantons")
async def get_cantons():
    cantons: List[Dict[str, str]] = []
    with open("../dataset/canton.csv") as file:
        reader = DictReader(file)
        for row in reader:
            cantons.append(row)
    return cantons
