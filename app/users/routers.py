from fastapi import APIRouter, Depends, HTTPException, status
from mongoengine import DoesNotExist

from app.commons.bearer import create_jwt, verify_jwt
from app.commons.password_hasher import hash_password, verify_password
from app.users.models import User
from app.users.schemas import LoginUser, RegisterUser

router = APIRouter(prefix="/users", tags=["users"])


def get_current_user(token: str):
    try:
        verify_jwt(token)
    except:
        pass


@router.post("/register-user")
def create_user(user: RegisterUser):
    user.password = hash_password(user.password)
    try:
        db_user = User.objects.get(email_address=user.email_address)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="email already exists"
        )
    except DoesNotExist:
        user = User(**user.model_dump())
        user.save()
        return user


@router.post("/login")
def login(user: LoginUser):

    try:
        db_user = User.objects.get(email_address=user.email_address)
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="invalid credentials"
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="invalid credentials"
        )

    token = create_jwt(str(db_user.id), db_user.email_address)

    return {"token": token}
