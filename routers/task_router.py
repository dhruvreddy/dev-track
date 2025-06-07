from fastapi import APIRouter, Depends

from dependency_injection import add_task_di, start_task_di, pause_task_di, resume_task_di, end_task_di

router = APIRouter(
    prefix="/task",
    tags=["Task"]
)


@router.post("/add_task")
def add_task_api(result = Depends(add_task_di)):
    return result

@router.post("/start_task")
def start_task_api(result = Depends(start_task_di)):
    return result

@router.post("/pause_task")
def start_task_api(result = Depends(pause_task_di)):
    return result

@router.post("/resume_task")
def start_task_api(result = Depends(resume_task_di)):
    return result

@router.post("/end_task")
def start_task_api(result = Depends(end_task_di)):
    return result