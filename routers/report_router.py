from fastapi import APIRouter, Depends

from dependency_injection import get_weekly_report_user_di, get_weekly_report_task_di

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

@router.get("/user_weekly")
def get_weekly_report_user_api(result = Depends(get_weekly_report_user_di)):
    return result

@router.get("/task_weekly")
def get_weekly_report_task_api(result = Depends(get_weekly_report_task_di)):
    return result