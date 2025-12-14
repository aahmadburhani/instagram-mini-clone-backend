from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Post, Follow


router = APIRouter(prefix="/feed", tags=["Feed"])

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def feed(user_id: int, db: Session = Depends(get_db)):
    following_ids = (
        db.query(Follow.following_id)
        .filter(Follow.follower_id == user_id)
    )

    posts = (
        db.query(Post)
        .filter(Post.user_id.in_(following_ids))
        .all()
    )

    return posts
