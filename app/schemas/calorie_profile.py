from pydantic import BaseModel, Field
from sqlalchemy import Column, Float
from typing import Optional

class CalorieProfileCreate(BaseModel):
    user_id: int
    daily_calories: float
    bmr: float
    tdee: float
    protein: float
    fat: float
    carb: float
    raw_response: str

class CalorieProfileResponse(BaseModel):
    id: int
    user_id: int
    daily_calories: float
    bmr: float
    tdee: float
    protein: float
    fat: float
    carb: float
    raw_response: str

    class Config:
        from_attributes = True
