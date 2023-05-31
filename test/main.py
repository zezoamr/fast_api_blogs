from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/h")
async def root(published:bool =  True, maybe: Optional[str] = None ):
    if published: return {"message": "Hello World"}
    else: return {"message":f"False cause published is {published} "}
    
@app.get("/info/{username}")
async def info(username: str):
    return {"message": {"about":"Hello again!", 'name':username, 'rest':'pending'}}

class blog(BaseModel):
    #super.__init__()
    title: str
    pagenumber: Optional[int]
    publipshed: Optional[bool]
    
@app.post("/blog")
async def info(request: blog):
    return {"message": f"blog is about {request.title}"}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)