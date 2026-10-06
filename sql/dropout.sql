SELECT e.user_id, u.name, e.course_id, c.title,
       COUNT(lp.lesson_id) FILTER (WHERE lp.completed) AS done,
       (SELECT COUNT(*) FROM lessons l WHERE l.course_id = e.course_id) AS total,
       NOW() - MAX(lp.completed_at) AS days_inactive
FROM enrollments e
JOIN users u ON u.id = e.user_id
JOIN courses c ON c.id = e.course_id
LEFT JOIN lesson_progress lp ON lp.user_id = e.user_id AND lp.completed
WHERE e.finished IS NULL
GROUP BY e.user_id, u.name, e.course_id, c.title
HAVING COUNT(lp.lesson_id) FILTER (WHERE lp.completed) <
       (SELECT COUNT(*) FROM lessons l WHERE l.course_id = e.course_id) * 0.3;
