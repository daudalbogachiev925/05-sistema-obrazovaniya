from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class CourseIn(BaseModel):
    title: str
    description: str | None = None
    price: float = 0
    author_id: int

@router.get("/")
def list_courses(published: bool = True, db: Session = Depends(get_session)):
    q = "SELECT * FROM courses WHERE published=:p" if published else "SELECT * FROM courses"
    return [dict(r._mapping) for r in db.execute(text(q), {"p": True}).fetchall()]

@router.post("/")
def create_course(data: CourseIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO courses (title, description, price, author_id, published)
        VALUES (:t,:d,:p,:a, FALSE) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0], "status": "created"}

@router.get("/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_session)):
    c = db.execute(text("SELECT * FROM courses WHERE id=:i"), {"i": course_id}).fetchone()
    if not c: raise HTTPException(404, "Курс не найден")
    lessons = db.execute(text("SELECT * FROM lessons WHERE course_id=:i ORDER BY position"),
                         {"i": course_id}).fetchall()
    return {**dict(c._mapping), "lessons": [dict(l._mapping) for l in lessons]}
