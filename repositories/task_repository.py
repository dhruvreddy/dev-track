from abc import ABC, abstractmethod
from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from enums import UserRole, TaskStatus
from models import User, Task
from schemas import TaskSchema

class TaskRepository(ABC):
    @abstractmethod
    def add_task(self, user: User, task: TaskSchema, session: Session):
        pass

    @abstractmethod
    def start_task(self, user: User, task_id: int, session: Session):
        pass

    @abstractmethod
    def pause_task(self, user: User, task_id: int, session: Session):
        pass

    @abstractmethod
    def resume_task(self, user: User, task_id: int, session: Session):
        pass

    @abstractmethod
    def end_task(self, user: User, task_id: int, session: Session):
        pass

class TaskRepositoryImpl(TaskRepository):
    def add_task(self, user: User, task: TaskSchema, session: Session):
        new_task = Task(
            title=task.title,
            description=task.description,
            user_id=user.id
        )
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
        return new_task

    def start_task(self, user: User, task_id: int, session: Session):
        if user.role == UserRole.VIEWER:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Viewers are not allowed to change the timeline"
            )

        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
        if not task:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

            # session.query(Task).filter(Task.id == task_id, Task.user_id == user.id).update({"start": start_time})
            # session.query(Task).filter(Task.id == task_id, Task.user_id == user.id).update({"resume": start_time})
            # session.query(Task).filter(Task.id == task_id, Task.user_id == user.id).update({"status": TaskStatus.IN_PROGRESS})

        if task.end:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Task has ended"
            )

        start_time = datetime.now()
        task.start = start_time
        task.resume = start_time
        task.status = TaskStatus.IN_PROGRESS

        session.commit()
        return {
            "message": "successful",
            "status": status.HTTP_200_OK
        }

    def pause_task(self, user: User, task_id: int, session: Session):
        if user.role == UserRole.VIEWER:
            raise HTTPException(status_code=401, detail="Not allowed")

        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        if not task.resume:
            raise HTTPException(status_code=400, detail="Task is not running")

        # total_time = session.query(Task.total_time_spent).filter(Task.id == task_id, Task.user_id == user.id).first()
        # pause_time = datetime.now()
        # total_time = task.total_time_spent
        # total_time += (pause_time - task.resume).total_seconds()
        # session.query(Task).filter(Task.id == task_id, Task.user_id == user.id).update({"pause": pause_time})
        # session.query(Task).filter(Task.id == task_id, Task.user_id == user.id).update({"resume": None})
        # session.query(Task).filter(Task.id == task_id, Task.user_id == user.id).update({"total_time_spent": total_time})

        pause_time = datetime.now()
        task.total_time_spent = round((task.total_time_spent or 0) + (pause_time - task.resume).total_seconds())
        task.pause = pause_time
        task.resume = None

        session.commit()
        return {
            "message": "successful",
            "status": status.HTTP_200_OK
        }

    def resume_task(self, user: User, task_id: int, session: Session):
        if user.role == UserRole.VIEWER:
            raise HTTPException(status_code=401, detail="Not allowed")

        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        if not task.pause:
            raise HTTPException(status_code=400, detail="Task is not paused")

        resume_time = datetime.now()
        task.resume = resume_time
        task.pause = None

        session.commit()
        return {
            "message": "successful",
            "status": status.HTTP_200_OK
        }

    def end_task(self, user: User, task_id: int, session: Session):
        if user.role == UserRole.VIEWER:
            raise HTTPException(status_code=401, detail="Not allowed")

        task = session.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        if not task.resume:
            raise HTTPException(status_code=400, detail="Task is not running")

        end_time = datetime.now()
        task.total_time_spent = round((task.total_time_spent or 0) + (end_time - task.resume).total_seconds())
        task.end = end_time
        task.resume = None
        task.pause = None

        session.commit()
        return {
            "message": "successful",
            "status": status.HTTP_200_OK
        }