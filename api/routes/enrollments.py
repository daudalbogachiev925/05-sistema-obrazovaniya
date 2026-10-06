from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class EnrollIn(BaseModel):
    user_id: int
    course_id: int

@router.post("/")
def enroll(data: EnrollIn, db: Session = Depends(get_session)):
    db.execute(text("""
        INSERT INTO enrollments (user_id, course_id) VALUES (:u,:c)
        ON CONFLICT DO NOTHING
    """), data.dict())
    db.commit()
    return {"status": "enrolled"}

@router.get("/user/{user_id}")
def my_courses(user_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("""
        SELECT c.id, c.title, e.started, e.finished
        FROM enrollments e JOIN courses c ON c.id=e.course_id
        WHERE e.user_id=:u
    """), {"u": user_id}).fetchall()]
