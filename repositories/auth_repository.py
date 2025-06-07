from abc import ABC, abstractmethod
from datetime import timedelta
from typing import Dict
from jose import JWTError
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from models import User
from utils import Hashing, Token


class AuthRepository(ABC):
    @abstractmethod
    def auth_user(self, user_details: OAuth2PasswordRequestForm, session: Session) -> str:
        pass

    @abstractmethod
    def get_user(self, token: str, session: Session) -> User:
        pass

class AuthRepositoryImpl(AuthRepository):
    def auth_user(self, user_details: OAuth2PasswordRequestForm, session: Session) -> Dict:
        user = session.query(User).filter(User.email == user_details.username).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        if not Hashing.verify_hash(str(user.password), user_details.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        token_data = {
            "sub": user.email,
            "name": user.name
        }
        return {
            "access_token": Token.encode_jwt(token_data, timedelta(minutes=30)),
            "token_type": "Bearer"
        }

    def get_user(self, token: str, session: Session) -> User:
        try:
            user_data = Token.decode_jwt(token)
            user = session.query(User).filter(User.email == user_data["sub"]).first()
            return user
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token"
            )