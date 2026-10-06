# Архитектура LMS

Пользователи → запись на курс → прохождение уроков → сертификат.

Таблицы:
- users, courses, lessons, quizzes
- enrollments, lesson_progress, certificates

Аналитика:
- progress.sql — прогресс по курсам
- engagement.sql — вовлечённость
- dropout.sql — отсев
- ML: RandomForest предсказывает вероятность отсева
