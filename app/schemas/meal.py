from pydantic import BaseModel
from typing import Optional

class MealBase(BaseModel):
    name: str
    description: str
    calories: Optional[float] = None
    protein: Optional[float] = None
    fat: Optional[float] = None
    carb: Optional[float] = None

class MealCreate(MealBase):
    pass

class MealResponse(MealBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
