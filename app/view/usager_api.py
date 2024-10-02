from fastapi import APIRouter, HTTPException, Depends, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.app_config.database_config import get_db
from app.schema.usager_schema import RequestUser, RequestUserSubscribe
from app.controller import usager_repository
from app.auth.auth import get_current_usager

usager_router = APIRouter()

# Fetch all usagers
@usager_router.get("/")
async def get(db:Session=Depends(get_db), current_user: str = Depends(get_current_usager)):
    _user = usager_repository.get_users(db, 0, 100)
    return {"users": _user}

# Inscription d'un usager
@usager_router.post("/subscribe")
async def create(request: RequestUserSubscribe, db:Session=Depends(get_db)):
    
    data = request.parameter
    print(data)
    age = usager_repository.calculate_age(data.date_naissance)
    print('aaa')
    if age:
        data.age = age
        usager_repository.add_user(db, data)

    return {"message": "Inscription réalisée avec succès!"}


# Creation d'un usager page admin
@usager_router.post("/create")
async def create(request: RequestUser, db:Session=Depends(get_db)):
    _user = usager_repository.add_user(db, request.parameter)
    return _user, 200

# Get usager by id
@usager_router.get("/{id}")
async def get_by_id(id: int, db:Session=Depends(get_db)):
    _user = usager_repository.fetch_user_by_id(db, id)
    return _user, 200

# Delete usager by id
@usager_router.delete("/{id}")
def delete(id: int, db:Session=Depends(get_db)):
    usager_repository.remove_user(db, id)
    message = f'Usager {id} supprimé avec succès'
    return message, 200