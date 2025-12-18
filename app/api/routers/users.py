from app.schemas.calorie_profile import CalorieProfileResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.core.database import get_db
from typing import List

router = APIRouter(prefix="/user", tags=["User"])
service = UserService()

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    return service.create_user(db, user_data)



@router.get("/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return service.get_all_users(db)

@router.get("/{user_id}/calorie_profile", response_model=CalorieProfileResponse)
def get_user_calorie_profile(user_id: int, db: Session = Depends(get_db)):
    return service.get_user_calorie_profile(db, user_id)

@router.get("/{user_id}/calorie_profile", response_model=CalorieProfileResponse)
def get_user_calorie_profile(user_id: int, db: Session = Depends(get_db)):
    return service.get_user_calorie_profile(db, user_id)