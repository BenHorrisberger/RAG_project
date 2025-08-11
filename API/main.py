from fastapi import FastAPI
from .endpoints import router

app = FastAPI(title = "aircraft_api")

app.include_router(router)
