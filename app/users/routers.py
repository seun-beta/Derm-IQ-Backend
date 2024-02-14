from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.commons.bearer import create_jwt, verify_jwt
from app.commons.password_hasher import hash_password, verify_password
from app.database import get_db
from app.users.models import User
from app.users.schemas import LoginUser, RegisterUser

router = APIRouter(prefix="/users", tags=["users"])


def get_current_user(token: str, db: Session = Depends(get_db)):
    try:
        verify_jwt(token)
    except:
        pass


@router.post("/register-user")
def create_user(user: RegisterUser, db: Session = Depends(get_db)):
    user.password = hash_password(user.password)
    db_user = db.query(User).filter(User.email_address == user.email_address).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="email already exists"
        )

    user = User(**user.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.post("/login")
def login(user: LoginUser, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email_address == user.email_address).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="invalid credentials"
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="invalid credentials"
        )

    token = create_jwt(db_user.id, db_user.email_address)

    return token
