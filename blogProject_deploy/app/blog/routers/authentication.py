from fastapi import APIRouter, Depends, status
from blog import schemas, database, oauth2
from sqlalchemy.orm import Session
from blog.repository import authentication


router = APIRouter(
    prefix="/login",
    tags=['login']
)

get_db = database.get_db

@router.post("",status_code=status.HTTP_202_ACCEPTED)
async def login(request: schemas.Login, db : Session = Depends(get_db)):
    authentication.login(request=request,db=db)