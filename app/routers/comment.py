from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Comment

router = APIRouter(prefix="/comment", tags=["Comment"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_comment(user_id: int, post_id: int, text: str, db: Session = Depends(get_db)):
    comment = Comment(
        user_id=user_id,
        post_id=post_id,
        text=text
    )
    db.add(comment)
    db.commit()
    return {"message": "comment posted successfully"}

