from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.meal import MealCreate, MealResponse
from app.services.meal_service import MealService

router = APIRouter(
    prefix="/user/{user_id}/meals",
    tags=["Meals"]
)

@router.post("/", response_model=MealResponse)
def add_meal(
    user_id: int,
    meal: MealCreate,
    db: Session = Depends(get_db)
):
    return MealService.add_meal(db, user_id, meal)

@router.get("/", response_model=List[MealResponse])
def get_meals(
    user_id: int,
    db: Session = Depends(get_db)
):
    return MealService.get_meals(db, user_id)
