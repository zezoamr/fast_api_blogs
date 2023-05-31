from pydantic import BaseModel
from typing import Optional, List

class Blog(BaseModel):
    #super.__init__()
    title: str
    pagenumber: Optional[int]
    publipshed: Optional[bool]
    user_id: int
    class Config():
        orm_mode = True
    
class User(BaseModel): 
    email: str
    id: int
    password: str
    name: str
    class Config():
        orm_mode = True
        
class Login(BaseModel):
    username: str #gonna be email for this
    password: str
    class Config():
        orm_mode = True
        
class responseUser(BaseModel):
    email: str
    name: str
    blogs: List[Blog] = []
    class Config():
        orm_mode = True
        
class showBlog(BaseModel): #can extend Blog too!
    title: str
    pagenumber: Optional[int]
    creator: Optional[responseUser] = None
    class Config():
        orm_mode = True                
        

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None