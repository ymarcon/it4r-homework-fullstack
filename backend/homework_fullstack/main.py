from typing import Union
import homework_fullstack.utils as hwu

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
    return hwu.read_data("../dataset/canton.csv").to_dict("index")


@app.get("/codes")
async def get_codes():
    return hwu.read_codes()
