from fastapi import APIRouter, Response, HTTPException, Depends, status

from dependency_injection import add_user_di, update_user_role_di


router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("/signup")
def user_signup_api(result = Depends(add_user_di)):
    return result

@router.post("/update_user_role")
def update_user_role_api(result = Depends(update_user_role_di)):
    return result