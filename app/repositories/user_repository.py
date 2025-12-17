from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

class UserRepository:

    def create(self, db: Session, user_data: UserCreate) -> User:
        user = User(**user_data.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    def get_users(self, db: Session) -> list[User]:
        return db.query(User).all() 