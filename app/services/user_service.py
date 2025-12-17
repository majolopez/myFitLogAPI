from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.models.user import User

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, db: Session, user_data: UserCreate) -> User:
        return self.repo.create(db, user_data)
    
    def get_all_users(self, db: Session) -> list[User]:
        return self.repo.get_users(db)