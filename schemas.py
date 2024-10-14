from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class Post(BaseModel):
    title:str
    content:str
    published: bool = True


class CreatePost(Post):
    pass

class ResponseUsers(BaseModel):
    name: str
    email:str
    # created_at: datetime

    class Config:
        orm_mode = True
        # from_atributes = True


class ResponsePost(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_id: int
    created_at: datetime
    owner: ResponseUsers

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: ResponsePost
    votes: int

class CreateUsers(BaseModel):
    
    name: str
    email: EmailStr
    password: str
    # created_at: datetime

class Login(BaseModel):
    email: str
    password: str
    

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id : Optional[str] = None

class Vote(BaseModel):
    post_id: int
    # user_id: int
    dir: int = Field(le=1)