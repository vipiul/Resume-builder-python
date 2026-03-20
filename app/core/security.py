from argon2 import PasswordHasher
from jose import jwt
from datetime import datetime, timedelta
from app.core.config import settings
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

ph = PasswordHasher()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

def hash_password(password: str) -> str:
    return ph.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    try:
        return ph.verify(hashed, plain)
    except Exception as e:
        print(f"Password verification failed: {e}")
        return False


def create_access_token(subject: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode = {"sub": subject, "exp": expire}
    return jwt.encode(to_encode, settings.jwt_secret, algorithm=settings.jwt_algo)


def create_refresh_token(subject: str) -> str:
    expire = datetime.utcnow() + timedelta(days=settings.refresh_token_expire_days)
    to_encode = {"sub": subject, "exp": expire}
    return jwt.encode(to_encode, settings.jwt_secret, algorithm=settings.jwt_algo)


def verify_token(token: str = Depends(oauth2_scheme)):
    payload = jwt.decode(token, settings.jwt_secret, algorithms=settings.jwt_algo)
    return payload