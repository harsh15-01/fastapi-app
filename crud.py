from sqlalchemy.orm import Session
from models import User


def get_user_by_email(db: Session, _id: int):
    return db.query(User).get(_id)
