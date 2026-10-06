from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

@router.get("/course/{course_id}")
def lessons_by_course(course_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(
        text("SELECT * FROM lessons WHERE course_id=:c ORDER BY position"),
        {"c": course_id}).fetchall()]

@router.get("/{lesson_id}")
def get_lesson(lesson_id: int, db: Session = Depends(get_session)):
    l = db.execute(text("SELECT * FROM lessons WHERE id=:i"), {"i": lesson_id}).fetchone()
    return dict(l._mapping) if l else {}
