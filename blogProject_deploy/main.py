from fastapi import FastAPI
from blog.routers import authentication
from blog import models
from blog.routers import blog,user,authentication
from blog.database import engine    

app = FastAPI()
models.Base.metadata.create_all(engine)
#uvicorn app.main:app --reload
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)