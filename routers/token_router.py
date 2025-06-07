from fastapi import APIRouter, Depends

from dependency_injection import auth_user_di

router = APIRouter(
    tags=["Token"]
)

@router.post("/token")
def token_api(result = Depends(auth_user_di)):
    return result
