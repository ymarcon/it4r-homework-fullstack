import homework_fullstack.utils as hwu
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, Response


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


@app.get("/cantons/{id}")
async def get_canton(id: int):
    """Get the data of a specific canton by its id number."""
    try:
        cantons = hwu.read_cantons().to_dict("index")
        # normalize code's case
        if id not in cantons:
            raise HTTPException(status_code=404, detail="Canton not found")
        data = cantons[id]
        return data
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/cantons")
async def get_cantons():
    """Get cantons data as a list."""
    try:
        return list(hwu.read_cantons().to_dict("index").values())
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/cantons-geo")
async def get_cantons_geo():
    """Get cantons data as a GeoJSON document."""
    try:
        return hwu.read_cantons_geo()
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/cantons-csv")
async def get_cantons_csv():
    """Get cantons data as a CSV file."""
    headers = {"Content-Disposition": 'attachment; filename="cantons.csv"'}
    try:
        cantons = hwu.read_cantons()
        # reorder columns
        cantons = cantons[["code", "title", "male", "female", "other"]]
        return Response(cantons.to_csv(), headers=headers, media_type="text/csv")
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/codes")
async def get_codes():
    """Get cantons normalized list."""
    return list(hwu.read_codes().to_dict("index").values())
