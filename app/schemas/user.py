from pydantic import BaseModel, Field
from sqlalchemy import Column, Float
from typing import Optional

class UserCreate(BaseModel):
    name: Optional[str]
    age: int = Field(gt=0)
    weight: str 
    height: str
    activity_level: str
    goal: str

class UserResponse(BaseModel):
    id: int
    name: Optional[str]
    age: int
    weight: float
    height: float
    activity_level: str
    goal: str

    class Config:
        from_attributes = True
