SELECT e.user_id, u.name, c.title,
       COUNT(lp.lesson_id) FILTER (WHERE lp.completed) AS completed,
       (SELECT COUNT(*) FROM lessons l WHERE l.course_id = e.course_id) AS total,
       ROUND(100.0 * COUNT(lp.lesson_id) FILTER (WHERE lp.completed) /
             NULLIF((SELECT COUNT(*) FROM lessons l WHERE l.course_id = e.course_id),0), 1) AS pct
FROM enrollments e
JOIN users u ON u.id = e.user_id
JOIN courses c ON c.id = e.course_id
LEFT JOIN lesson_progress lp ON lp.user_id = e.user_id
WHERE e.course_id = $1
GROUP BY e.user_id, u.name, c.title, e.course_id
ORDER BY pct DESC;
