
from sqlalchemy.orm import Session
from blog import models, schemas
from fastapi import HTTPException,status,Response

def create(request: schemas.Blog, db : Session, **kwargs):
    new_blog = models.Blog(title = request.title, user_id=request.user_id, publipshed = request.publipshed, pagenumber = request.pagenumber)
    db.add(new_blog)
    db.commit()
    db.refresh()
    
def all(db : Session, **kwargs):
    blogs = db.query(models.Blog).all()
    return blogs

def show(id, response : Response, db : Session, **kwargs):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"blog with id {id} not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"detail": f"blog with id {id} not found"}
    return blog

def destroy(id, db : Session, **kwargs):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'

def destroy(id, request: schemas.Blog, db : Session, **kwargs):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"blog with id {id} not found")
    blog.update(request.dict(), synchronize_session=False)
    db.commit()
    return 'updated'