from enum import Enum

class TaskStatus(Enum):
    TO_DO = "to_do"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class TaskPriority(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"