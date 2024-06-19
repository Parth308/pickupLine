from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from langserve import add_routes
from chain import chain
from typing import Dict

app = FastAPI(
    title="Pickup Lines API",
    description="Pickup Lines Generation API",
)

add_routes(app, chain, path="/pickup")
app.mount(
    "/static",
    StaticFiles(
        directory="static"
    ),
    name="static"
)

@app.get("/", response_class=FileResponse)
async def root():
    return FileResponse(
        "index.html"
    )

@app.get("/ping", response_model=Dict)
async def root():
    return {
        "message": "yes"
    }

