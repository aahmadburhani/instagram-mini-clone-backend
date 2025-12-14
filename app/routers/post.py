from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Post

router = APIRouter(prefix="/post", tags=["Post"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_new_post(image_url: str, caption: str, user_id: int, db: Session = Depends(get_db)):
    post = Post(
        image_url=image_url,
        caption=caption,
        user_id=user_id
    )
    db.add(post)
    db.commit()
    return {
    "status": "success",
    "info": "post uploaded",
    "user": user_id
}
