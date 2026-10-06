from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class ProgressIn(BaseModel):
    user_id: int
    lesson_id: int

@router.post("/complete")
def complete(data: ProgressIn, db: Session = Depends(get_session)):
    db.execute(text("""
        INSERT INTO lesson_progress (user_id, lesson_id, completed, completed_at)
        VALUES (:u, :l, TRUE, NOW())
        ON CONFLICT (user_id, lesson_id)
        DO UPDATE SET completed = TRUE, completed_at = NOW()
    """), data.dict())
    db.commit()
    return {"status": "ok"}

@router.get("/user/{user_id}/course/{course_id}")
def progress(user_id: int, course_id: int, db: Session = Depends(get_session)):
    row = db.execute(text("""
        SELECT
          (SELECT COUNT(*) FROM lessons WHERE course_id=:c) AS total,
          (SELECT COUNT(*) FROM lesson_progress lp
           JOIN lessons l ON l.id=lp.lesson_id
           WHERE lp.user_id=:u AND l.course_id=:c AND lp.completed) AS done
    """), {"u": user_id, "c": course_id}).fetchone()
    total, done = row
    pct = round(100.0 * done / total, 1) if total else 0
    return {"total": total, "done": done, "pct": pct}
