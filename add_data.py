import json
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, joinedload
from models import Part, Question, Answer

engine = create_engine('sqlite:///questions.db')
SessionLocal = sessionmaker(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    with open('structured_questions.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        for test in data:
            title = test.get("title")
            chapter_insert = Part(name=title)
            questions = test.get("subsections")[0].get("questions")
            for question in questions:
                answers = question.get("options")
                correct = question.get("correct")
                question_insert = Question(text=question.get("question"),
                                           part=chapter_insert)
                for i, answer in enumerate(answers):
                    answer_insert = Answer(text=answer,
                                           is_correct=(i == correct),
                                           question=question_insert)
                    db.add(answer_insert)
                db.add(question_insert)
            db.add(chapter_insert)
        db.commit()

