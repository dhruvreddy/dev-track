from fastapi import APIRouter, Depends

from dependency_injection import add_task_di, start_task_di, pause_task_di, resume_task_di, end_task_di, update_task_priority_di

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)


@router.post("/add_task")
def add_task_api(result = Depends(add_task_di)):
    return result

@router.patch("/start_task")
def start_task_api(result = Depends(start_task_di)):
    return result

@router.patch("/pause_task")
def start_task_api(result = Depends(pause_task_di)):
    return result

@router.patch("/resume_task")
def start_task_api(result = Depends(resume_task_di)):
    return result

@router.patch("/end_task")
def start_task_api(result = Depends(end_task_di)):
    return result

@router.patch("/update_task_priority")
def update_task_priority_api(result = Depends(update_task_priority_di)):
    return result