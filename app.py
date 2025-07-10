from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, joinedload
from models import Part, Question, Answer
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
app.mount("/css", StaticFiles(directory="css"), name="css")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://kusvonus.ru"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_index():
    return FileResponse("templates/index.html")

engine = create_engine('sqlite:///questions.db')
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

@app.get("/questions")
def read_questions(db: Session = Depends(get_db)):
    return db.query(Part).options(
        joinedload(Part.question).joinedload(Question.answer)
    ).all()
