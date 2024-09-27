from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.view.usager_api import usager_router
from app.view.login_api import login_router
from app.view.admin_api import admin_router
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
    allow_headers=["Authorization", "Content-Type", "Accept"]
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"Erreur inattendue: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Erreur serveur interne. Veuillez réessayer plus tard."},
    )

Base.metadata.create_all(bind=engine)

@app.get("/")
def index():
    return {"main": "Helloworld"}

app.include_router(usager_router, prefix='/usager', tags=['usager'])
app.include_router(login_router, prefix='/login', tags=['login'])
app.include_router(admin_router, prefix='/admin', tags=['admin'])