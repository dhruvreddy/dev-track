# Python Imports
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

# Local Imports
from enums import UserRole, TaskPriority
from utils import engine, Session as Con
from models import Base
from models import User
from schemas import UserSchema, TaskSchema
from repositories import UserRepositoryImpl, AuthRepositoryImpl, TaskRepositoryImpl, ReportRepositoryImpl

oauth = OAuth2PasswordBearer("/token")

user_repo = UserRepositoryImpl()

auth_repo = AuthRepositoryImpl()

task_repo = TaskRepositoryImpl()

report_repo = ReportRepositoryImpl()

#Database

def create_all_di():
    return Base.metadata.create_all(engine)

def get_db():
    db = Con()
    try:
        yield db
    finally:
        db.close()

# Auth

def auth_user_di(user_details: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    return auth_repo.auth_user(user_details=user_details, session=session)

def get_user_di(token: str = Depends(oauth), session: Session = Depends(get_db)):
    return auth_repo.get_user(token=token, session=session)

# User

def add_user_di(user: UserSchema, session: Session = Depends(get_db)):
    return user_repo.user_signup(user=user, session=session)

def update_user_role_di(role: UserRole, session: Session = Depends(get_db) , user = Depends(get_user_di)):
    return user_repo.update_user_role(user=user, role=role, session=session)

# Task

def add_task_di(task: TaskSchema, session: Session = Depends(get_db), user: User = Depends(get_user_di)):
    return task_repo.add_task(user=user, task=task, session=session)

def start_task_di(task_id: int, session: Session = Depends(get_db), user: User = Depends(get_user_di)):
    return task_repo.start_task(user=user, task_id=task_id, session=session)

def pause_task_di(task_id: int, session: Session = Depends(get_db), user: User = Depends(get_user_di)):
    return task_repo.pause_task(user=user, task_id=task_id, session=session)

def resume_task_di(task_id: int, session: Session = Depends(get_db), user: User = Depends(get_user_di)):
    return task_repo.resume_task(user=user, task_id=task_id, session=session)

def end_task_di(task_id: int, session: Session = Depends(get_db), user: User = Depends(get_user_di)):
    return task_repo.end_task(user=user, task_id=task_id, session=session)

def update_task_priority_di(priority: TaskPriority, task_id: int, session: Session = Depends(get_db), user: User = Depends(get_user_di)):
    return task_repo.update_task_priority(priority=priority, task_id=task_id, session=session, user=user)

# Report

def get_weekly_report_user_di(user = Depends(get_user_di), session = Depends(get_db)):
    return report_repo.get_weekly_report_user(user=user, session=session)

def get_weekly_report_task_di(task_id: int, user = Depends(get_user_di), session = Depends(get_db)):
    return report_repo.get_weekly_report_task(task_id=task_id, user=user, session=session)

# Repository Classes

def get_auth_repository() ->AuthRepositoryImpl:
    return AuthRepositoryImpl()

def get_user_repository() -> UserRepositoryImpl:
    return UserRepositoryImpl()

def get_task_repository() -> TaskRepositoryImpl:
    return TaskRepositoryImpl()
