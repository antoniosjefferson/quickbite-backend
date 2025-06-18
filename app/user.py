from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.models import User
from app.database import get_session

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/users/", response_model=list[User])
def read_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return users