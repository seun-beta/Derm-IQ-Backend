from datetime import datetime, timedelta

import jwt

from app.config import settings


def create_jwt(user_id: str, email: str) -> str:
    exp = datetime.now() + timedelta(minutes=settings.jwt_access_token_exp_minutes)
    payload = {"user_id": user_id, "email": email, "exp": exp}
    token = jwt.encode(
        payload=payload, key=settings.jwt_secret, algorithm=settings.jwt_algorithm
    )
    return token


def verify_jwt(token: str):
    try:
        payload = jwt.decode(
            jwt=token, key=settings.jwt_secret, algorithms=[settings.jwt_algorithm]
        )
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        return "invalid jwt"

    user_id = payload.get("user_id")
    return user_id
