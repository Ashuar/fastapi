from fastapi import Depends, status, HTTPException, APIRouter
from database import get_db
import models
import models, schemas, utils
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ResponseUsers)
def create_user(user: schemas.CreateUsers, db: Session = Depends(get_db)):
    hashed_password = utils.pwd_context.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.get("/{id}", response_model=schemas.ResponseUsers)
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    # user = db.query(models.User).all()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Wrong Id please enter a valid ID")
    
    return user