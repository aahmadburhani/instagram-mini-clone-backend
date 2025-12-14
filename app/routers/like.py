from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Like

router = APIRouter(prefix="/like", tags=["Like"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def like_post(user_id: int, post_id: int, db: Session = Depends(get_db)):
    new_like = Like(
    user_id=user_id,
    post_id=post_id
)

    db.add(new_like)
    db.commit()
    return {"message": "Post liked"}

@router.delete("/")
def unlike_post(user_id: int, post_id: int, db: Session = Depends(get_db)):
    like = db.query(Like).filter(
        Like.user_id == user_id,
        Like.post_id == post_id
    ).first()

    if like is None:
        return {"message": "user has not liked this post yet"}


    db.delete(like)
    db.commit()
    return {"message": "Post unliked"}
