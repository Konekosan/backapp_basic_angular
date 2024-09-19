from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.view.usager_api import usager_router
from app.app_config.database import Base
from app.app_config.database import engine

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "Accept"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def index():
    return {"main": "Helloworld"}

app.include_router(usager_router, prefix='/usager', tags=['usager'])