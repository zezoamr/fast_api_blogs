from sqlalchemy.orm import Session
from blog import models, schemas,hashing,JWTtoken
from fastapi import HTTPException,status

def login(request: schemas.Login, db : Session, **kwargs):
    user = db.query(models.User).filter(models.user.email==request.username).first()
    passhash = hashing.hash.verify( requestpass=request.password, userpass=user.password)
    if (not user) or (not passhash) :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"invalid credintials")
    
    access_token = JWTtoken.create_access_token(
        data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}