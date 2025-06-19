import sqlite3

conn = sqlite3.connect('questions.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS question
               (question_id SERIAL PRIMARY KEY,
               question_number VARCHAR(10),
               qestion_test TEXT NOT NULL)''')

cursor.execute('''CREATE TABLE answers (
    answer_id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions(question_id) ON DELETE CASCADE,
    answer_text TEXT NOT NULL,
    is_correct BOOLEAN DEFAULT FALSE)''')

conn.commit()
