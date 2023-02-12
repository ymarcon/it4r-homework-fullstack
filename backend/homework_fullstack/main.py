import homework_fullstack.utils as hwu
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse


app = FastAPI()

# CORS
origins = os.getenv("ORIGINS", "http://localhost:5173").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return RedirectResponse("/cantons")


@app.get("/cantons/{code}")
async def get_canton(code: str):
    """Get the data of a specific canton."""
    try:
        cantons = hwu.read_cantons()
        # normalize code's case
        codestr = code.upper()
        if codestr not in cantons:
            raise HTTPException(status_code=404, detail="Canton not found")
        data = cantons[codestr]
        return data
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/cantons")
async def get_cantons():
    """Get cantons data as a list."""
    try:
        return list(hwu.read_cantons().values())
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/codes")
async def get_codes():
    """Get cantons codes."""
    return hwu.read_codes()
