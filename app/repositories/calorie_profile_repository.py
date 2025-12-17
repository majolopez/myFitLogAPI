from sqlalchemy.orm import Session
from app.models.calorie_profile import CalorieProfile
from app.schemas.calorie_profile import CalorieProfileCreate

class CalorieProfileRepository:

    def create(self, db: Session, calorie_profile_data: CalorieProfileCreate) -> CalorieProfile:
        calorie_profile = CalorieProfile(**calorie_profile_data.model_dump())
        db.add(calorie_profile)
        db.commit()
        db.refresh(calorie_profile)
        return calorie_profile

    def get_calorie_profiles(self, db: Session) -> list[CalorieProfile]:
        return db.query(CalorieProfile).all() 
    
    def get_calorie_profile(self, db: Session, user_id: int) -> list[CalorieProfile]:
        return db.query(CalorieProfile).filter(CalorieProfile.user_id == user_id).all()