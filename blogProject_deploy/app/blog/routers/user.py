from fastapi import APIRouter,Depends,status
from blog import database, schemas, oauth2
from sqlalchemy.orm import Session
from blog.repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users'], dependencies=[Depends(oauth2.get_current_user)]
)

get_db = database.get_db

@router.post("/add",status_code=status.HTTP_201_CREATED,  response_model=schemas.responseUser)
async def create(request: schemas.User, db : Session = Depends(get_db)):
    return user.create(db=db,request=request)

@router.get("/{id}",status_code=status.HTTP_201_CREATED,  response_model=schemas.responseUser)
async def get_user(id:int, db : Session = Depends(get_db)):
    return user.get_user(id=id, db=db)