import json
from abc import ABC, abstractmethod
from datetime import datetime
from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session

from models import User, Task


class ReportRepository(ABC):
    @abstractmethod
    def get_weekly_report_user(self, user: User, session: Session):
        pass

    @abstractmethod
    def get_weekly_report_task(self, task_id: int, user: User, session: Session):
        pass

class ReportRepositoryImpl(ReportRepository):
    def get_weekly_report_user(self, user: User, session: Session):
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="UNAUTHORIZED"
            )
        tasks = session.query(Task).filter(Task.user_id == user.id).all()
        all_tasks = [
            {
                "title": task.title,
                "description": task.description,
                "status": task.status.value,
                "priority": task.priority.value,
                "created_at": task.created_at.isoformat() if task.created_at else None,
                "started_at": task.start.isoformat() if task.start else None,
                "paused_at": task.pause.isoformat() if task.pause else None,
                "resumed_at": task.resume.isoformat() if task.resume else None,
                "ended_at": task.end.isoformat() if task.end else None,
                "time_spent": task.total_time_spent
            }
            for task in tasks
        ]
        file_name = f"weekly_report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
        json_data = json.dumps(all_tasks, indent=4)
        return Response(
            status_code=status.HTTP_200_OK,
            content=json_data,
            media_type="application/json",
            headers={
            "Content-Disposition": f"attachment; filename={file_name}"
            }
        )

    def get_weekly_report_task(self, task_id: int, user: User, session: Session):
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="UNAUTHORIZED"
            )
        tasks = session.query(Task).filter(Task.id == task_id).all()
        all_tasks = [
            {
                "title": task.title,
                "description": task.description,
                "status": task.status.value,
                "priority": task.priority.value,
                "created_at": task.created_at.isoformat() if task.created_at else None,
                "started_at": task.start.isoformat() if task.start else None,
                "paused_at": task.pause.isoformat() if task.pause else None,
                "resumed_at": task.resume.isoformat() if task.resume else None,
                "ended_at": task.end.isoformat() if task.end else None,
                "time_spent": task.total_time_spent
            }
            for task in tasks
        ]
        file_name = f"weekly_report_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
        json_data = json.dumps(all_tasks, indent=4)
        return Response(
            status_code=status.HTTP_200_OK,
            content=json_data,
            media_type="application/json",
            headers={
            "Content-Disposition": f"attachment; filename={file_name}"
            }
        )