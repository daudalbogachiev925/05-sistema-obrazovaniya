SELECT c.id, c.title,
       COUNT(DISTINCT e.user_id) AS students,
       COUNT(DISTINCT lp.user_id) FILTER (WHERE lp.completed) AS active,
       ROUND(AVG(lp.completed::int) * 100, 1) AS avg_progress
FROM courses c
LEFT JOIN enrollments e ON e.course_id = c.id
LEFT JOIN lessons l ON l.course_id = c.id
LEFT JOIN lesson_progress lp ON lp.lesson_id = l.id
GROUP BY c.id
ORDER BY students DESC;
