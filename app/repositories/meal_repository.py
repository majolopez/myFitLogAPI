from sqlalchemy.orm import Session
from app.models.meal import Meal
from app.schemas.meal import MealCreate

class MealRepository:

    @staticmethod
    def create(db: Session, user_id: int, meal: MealCreate):
        db_meal = Meal(
            name=meal.name,
            description=meal.description,
            user_id=user_id,
            calories=meal.calories,
            protein=meal.protein,
            fat=meal.fat,
            carb=meal.carb
        )
        db.add(db_meal)
        db.commit()
        db.refresh(db_meal)
        return db_meal

    @staticmethod
    def get_by_user(db: Session, user_id: int):
        return (
            db.query(Meal)
            .filter(Meal.user_id == user_id)
            .order_by(Meal.id.desc())
            .all()
        )
