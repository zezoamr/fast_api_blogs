from typing import List
from fastapi import APIRouter, Depends, status, Response
from blog import schemas, database, oauth2
from sqlalchemy.orm import Session
from blog.repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs'], dependencies=[Depends(oauth2.get_current_user)] #,current_user: schemas.User = Depends(oauth2.get_current_user
)

get_db = database.get_db

@router.post("/add",status_code=status.HTTP_201_CREATED)
async def create(request: schemas.Blog, db : Session = Depends(get_db)):
    blog.create(request=request,db=db)
    
@router.get('/all', response_model=List[schemas.showBlog])
async def all(db : Session = Depends(get_db)):
    return blog.all(db=db)

@router.get('/{id}', status_code=status.HTTP_302_FOUND, response_model=schemas.showBlog)
async def show(id, response : Response, db : Session = Depends(get_db)):
    return blog.show(id=id, response=response, db=db)

@router.delete('/{id}', status_code=status.HTTP_200_OK)
async def destroy(id, db : Session = Depends(get_db)):
    return blog.destroy(id=id,db=db)

@router.put('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id, request: schemas.Blog, db : Session = Depends(get_db)):
    return blog.destroy(id=id, request=request, db=db)