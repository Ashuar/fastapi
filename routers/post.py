from fastapi import FastAPI, Depends, status, HTTPException, APIRouter
from database import get_db
import models
import models, schemas
from sqlalchemy.orm import Session
from typing import List
import oauth2
from sqlalchemy import func

router = APIRouter(
    prefix="/create",
    tags=["Posts"]
)

@router.get("/", response_model=List[schemas.PostOut])
# @router.get("/")
def root(db: Session = Depends(get_db), limit:int=10):
    #user_id:int = Depends(oauth2.current_user),
    post = db.query(models.Post).limit(limit).all()
    result = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote,
                 models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()
    # results = List[result]
    return result


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponsePost)
def create(post: schemas.CreatePost, db: Session = Depends(get_db), user_id:int= Depends(oauth2.current_user)) :
    
    new_post = models.Post(created_id = user_id.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return  new_post

@router.get("/{id}", response_model=schemas.ResponsePost)
def post(id:int, db: Session = Depends(get_db),  user_id:int= Depends(oauth2.current_user)):

    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wrong Id please enter a valid ID")

    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id:int, db: Session = Depends(get_db),  user_id:int= Depends(oauth2.current_user)):

    post = db.query(models.Post).filter(models.Post.id == id)

    deleted_post = post.first()

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wrong id please enter a valid ID")
    
    if deleted_post.created_id != user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")
    # deleted_post.delete(synchronize_session=False)
    db.delete(deleted_post)
    db.commit()
    
    return deleted_post

@router.put("/{id}", response_model=schemas.ResponsePost)
def update_post(id: int, post: schemas.CreatePost, db: Session = Depends(get_db),  user_id:int= Depends(oauth2.current_user)):

    updated_post = db.query(models.Post).filter(models.Post.id ==id)
    post_new = updated_post.first()

    if post_new == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wrong Id please enter a valid ID")
    
    if post_new.created_id != user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not Authorized")

    updated_post.update(post.model_dump(), synchronize_session=False)
    
    db.commit()
    return updated_post.first()

