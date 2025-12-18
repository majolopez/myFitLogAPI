from sqlalchemy.orm import Session
from app.repositories.meal_repository import MealRepository
from app.schemas.meal import MealCreate
from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MEAL_ANALYSIS_SYSTEM_PROMPT = """
You are a nutrition analysis engine.

Rules:
- Respond ONLY with valid JSON
- Do NOT include markdown
- Do NOT include explanations
- Do NOT include units in values
- All numbers must be floats
- If unsure, make a conservative estimate

JSON schema:
{
  "calories": float,
  "protein": float,
  "fat": float,
  "carb": float
}
"""

class MealService:
    def __init__(self):
        self.repo = MealRepository()
        self.client = OpenAI()

    @staticmethod
    def add_meal(db: Session, user_id: int, meal: MealCreate):
        nutrition = analyze_meal_with_openai(
            meal.name,
            meal.description
        )

        meal.calories = nutrition["calories"]
        meal.protein = nutrition["protein"]
        meal.fat = nutrition["fat"]
        meal.carb = nutrition["carb"]

        return MealRepository.create(
            db=db,
            user_id=user_id,
            meal=meal
        )

    @staticmethod
    def get_meals(db: Session, user_id: int):
        return MealRepository.get_by_user(db, user_id)
    

def analyze_meal_with_openai(meal_name: str, description: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,  # 🔒 deterministic
        messages=[
            {
                "role": "system",
                "content": MEAL_ANALYSIS_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": build_meal_prompt(meal_name, description)
            }
        ]
    )

    raw_content = response.choices[0].message.content

    try:
        parsed = json.loads(raw_content)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON from OpenAI: {raw_content}")

    # Validate expected keys
    required_keys = {"calories", "protein", "fat", "carb"}
    if not required_keys.issubset(parsed.keys()):
        raise ValueError(f"Missing keys in OpenAI response: {parsed}")

    return parsed

def build_meal_prompt(meal_name: str, description: str) -> str:
    return f"""
        Meal name: {meal_name}
        Meal description: {description}

        Estimate total nutritional values for this meal.
        """
