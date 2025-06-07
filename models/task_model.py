from sqlalchemy import Integer, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from datetime import datetime
from .base_model import Base
# from .user_model import User
from enums import TaskStatus, TaskPriority

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[TaskStatus] = mapped_column(Enum(TaskStatus), default=TaskStatus.TO_DO)
    priority: Mapped[TaskPriority] = mapped_column(Enum(TaskPriority), default=TaskPriority.LOW)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    start: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    pause: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    resume: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    end: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    total_time_spent: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="tasks")
