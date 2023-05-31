from sqlalchemy.orm import Session
from blog import models, schemas
from fastapi import HTTPException,status
from blog import hashing

def create(db: Session, request: schemas.User, **kwargs):
    hashedpass = hashing.hash.bcrypt(request.password)
    new_user = models.User(**request.dict()) #models.User(name=request.name,email=request.email,password=hashedpass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id:int, db : Session, **kwargs):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with id {id} not found")
    return user