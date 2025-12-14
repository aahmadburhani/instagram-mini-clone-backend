from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Follow

router = APIRouter(prefix="/follow", tags=["Follow"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def follow_user(follower_id: int, following_id: int, db: Session = Depends(get_db)):
    follow = Follow(
        follower_id=follower_id,
        following_id=following_id
    )
    db.add(follow)
    db.commit()
    return {"message": "User followed"}

@router.delete("/")
def unfollow_user(follower_id: int, following_id: int, db: Session = Depends(get_db)):
    follow = db.query(Follow).filter(
        Follow.follower_id == follower_id,
        Follow.following_id == following_id
    ).first()

    if not follow:
        return {"error": "Follow relationship not found"}

    db.delete(follow)
    db.commit()
    return {"message": "User unfollowed"}
