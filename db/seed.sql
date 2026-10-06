INSERT INTO users (email, name, role) VALUES
('teacher@mail.ru','Иван','teacher'),
('a@mail.ru','Аня','student'),
('b@mail.ru','Боря','student'),
('c@mail.ru','Вика','student');

INSERT INTO courses (title, description, price, author_id, published) VALUES
('SQL с нуля', 'Основы работы с базами данных', 3000, 1, TRUE),
('Python для анализа данных', 'Pandas, NumPy, визуализация', 5000, 1, TRUE);

INSERT INTO lessons (course_id, title, position, duration_min) VALUES
(1,'Введение',1,20),(1,'SELECT и WHERE',2,40),(1,'JOIN',3,60),
(1,'Группировки',4,45),(1,'Оконные функции',5,90),
(2,'Установка Python',1,15),(2,'Pandas',2,80),(2,'Визуализация',3,60);

INSERT INTO enrollments (user_id, course_id) VALUES
(2,1),(3,1),(4,1),(2,2);

INSERT INTO lesson_progress (user_id, lesson_id, completed, completed_at) VALUES
(2,1,TRUE,'2024-01-02'),(2,2,TRUE,'2024-01-03'),(2,3,TRUE,'2024-01-05'),
(3,1,TRUE,'2024-01-02'),
(4,1,TRUE,'2024-01-02');
