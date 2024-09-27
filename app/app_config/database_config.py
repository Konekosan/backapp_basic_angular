from app.app_config.database import SessionLocal
from fastapi import HTTPException
import logging

loggers = logging.getLogger(__name__)

def _print(text: str, log_level='info'):
    print(text)
    getattr(loggers, log_level)(text)

def get_db():
    db = SessionLocal()
    try:
        yield db
    # except Exception as e:
    #     raise HTTPException(
    #         status_code=500,
    #         detail="Erreur lors de la connexion à la base de données.",
    #     ) from e
    finally:
        db.close()