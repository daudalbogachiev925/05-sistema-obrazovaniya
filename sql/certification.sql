SELECT u.name, c.title, cert.number, cert.issued
FROM certificates cert
JOIN users u ON u.id = cert.user_id
JOIN courses c ON c.id = cert.course_id
ORDER BY cert.issued DESC;
