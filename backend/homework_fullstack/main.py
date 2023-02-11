from typing import Union
import homework_fullstack.utils as hwu

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/cantons")
async def get_cantons():
    cantons = hwu.read_data("../dataset/canton.csv")
    cantons = cantons.rename(
        columns={"Canton": "title", "Hommes": "male", "Femmes": "female"}
    )
    cantons["other"] = 0
    cantons = cantons.drop(columns=["Suisses", "Etrangers"])
    return cantons.to_dict("index")


@app.get("/codes")
async def get_codes():
    return hwu.read_codes()
