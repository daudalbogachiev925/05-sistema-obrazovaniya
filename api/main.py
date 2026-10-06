from fastapi import FastAPI
from routes import courses, lessons, enrollments, progress

app = FastAPI(title="LMS API")

app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(lessons.router, prefix="/lessons", tags=["lessons"])
app.include_router(enrollments.router, prefix="/enrollments", tags=["enrollments"])
app.include_router(progress.router, prefix="/progress", tags=["progress"])

@app.get("/health")
def health(): return {"status": "ok"}
