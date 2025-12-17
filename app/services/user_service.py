from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.repositories.calorie_profile_repository import CalorieProfileRepository
from app.schemas.user import UserCreate
from app.schemas.calorie_profile import CalorieProfileCreate
from app.models.user import User
from app.models.calorie_profile import CalorieProfile
from openai import OpenAI
import json
import os

class UserService:
    def __init__(self):
        self.repo = UserRepository()
        self.calorie_profile_repo = CalorieProfileRepository()
        self.client = OpenAI()

    def get_calorie_profile(self, user: User) -> dict:
        prompt_system = """
        You are a nutrition calculation engine.
        You must ONLY return valid JSON.
        Do not include explanations, markdown, or extra text.

        Use the Mifflin-St Jeor equation to calculate BMR.
        Then calculate TDEE based on activity level.
        Then adjust calories based on the goal.

        Activity level multipliers:
        - sedentary: 1.2
        - light: 1.375
        - moderate: 1.55
        - high: 1.725
        - athlete: 1.9

        Goal adjustments:
        - lose_fat: -20% calories
        - maintain: 0%
        - gain_muscle: +15% calories

        Macronutrient distribution:
        - Protein: 2.0 grams per kg of body weight
        - Fat: 25% of total calories
        - Carbohydrates: remaining calories

        Return the result strictly in this JSON format:

        {
        "bmr": number,
        "tdee": number,
        "daily_calories": number,
        "macros": {
            "protein_g": number,
            "fat_g": number,
            "carbs_g": number
        }
        }
        """

        prompt_user = f"""
        User data:
        - Age: {user.age}
        - Weight: {user.weight} kg
        - Height: {user.height} cm
        - Activity level: {user.activity_level}
        - Goal: {user.goal}
        - Sex: {user.sex}
        """

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt_system},
                {"role": "user", "content": prompt_user},
            ],
            temperature=0,
        )

        content = response.choices[0].message.content
        data = json.loads(content)
        calorie_profile = CalorieProfileCreate(
            user_id=user.id,
            daily_calories=float(data["daily_calories"]),
            bmr=float(data["bmr"]),
            tdee=float(data["tdee"]),
            protein=float(data["macros"]["protein_g"]),
            fat=float(data["macros"]["fat_g"]),
            carb=float(data["macros"]["carbs_g"]),
            raw_response=content
        )
        return calorie_profile

    def create_user(self, db: Session, user_data: UserCreate) -> User:
        user = self.repo.create(db, user_data)
        calorie_profile = self.get_calorie_profile(user)
        self.calorie_profile_repo.create(db, calorie_profile)
        print("Calorie Profile:", calorie_profile)
        return user


    def get_all_users(self, db: Session) -> list[User]:
        return self.repo.get_users(db)
        