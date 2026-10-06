CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    name TEXT,
    role TEXT DEFAULT 'student',
    created TIMESTAMP DEFAULT NOW()
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price NUMERIC(10,2),
    author_id BIGINT REFERENCES users(id),
    published BOOLEAN DEFAULT FALSE,
    created TIMESTAMP DEFAULT NOW()
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    course_id INT REFERENCES courses(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    content TEXT,
    position INT NOT NULL,
    duration_min INT
);

CREATE TABLE quizzes (
    id SERIAL PRIMARY KEY,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
);

CREATE TABLE enrollments (
    user_id BIGINT REFERENCES users(id),
    course_id INT REFERENCES courses(id),
    started TIMESTAMP DEFAULT NOW(),
    finished TIMESTAMP,
    PRIMARY KEY (user_id, course_id)
);

CREATE TABLE lesson_progress (
    user_id BIGINT REFERENCES users(id),
    lesson_id INT REFERENCES lessons(id),
    completed BOOLEAN DEFAULT FALSE,
    completed_at TIMESTAMP,
    PRIMARY KEY (user_id, lesson_id)
);

CREATE TABLE certificates (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT REFERENCES users(id),
    course_id INT REFERENCES courses(id),
    number TEXT UNIQUE,
    issued TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_lessons_course ON lessons(course_id);
CREATE INDEX idx_progress_user ON lesson_progress(user_id);
