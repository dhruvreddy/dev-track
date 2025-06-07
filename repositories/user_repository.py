from abc import ABC, abstractmethod
from fastapi import Response, status, HTTPException
from sqlalchemy.orm import Session

from enums import UserRole
from models import User
from schemas import UserSchema
from utils import Hashing

class UserRepository(ABC):
    @abstractmethod
    def user_signup(self, user: UserSchema, session: Session):
       pass

    @abstractmethod
    def update_user_role(self, user: User, role: UserRole, session: Session):
        pass

class UserRepositoryImpl(UserRepository):
    def user_signup(self, user: UserSchema, session: Session) -> User:
        existing = session.query(User).filter(User.email == user.email).first()
        if existing:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        new_user = User(
            name=user.name,
            email=user.email,
            password=Hashing.get_hash(user.password)
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

    def update_user_role(self, user: User, role: UserRole, session: Session):
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )
        if user.role == role:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Selected role is same as current role"
            )
        user.role = role
        session.commit()
        return {
            "message": "user role updated",
            "status": status.HTTP_200_OK
        }