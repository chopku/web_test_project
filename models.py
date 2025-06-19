from sqlalchemy import Column, Integer, String, Boolean, create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase): pass

class Part(Base):
    __tablename__ = 'part'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    question = relationship("Question", back_populates="part", cascade="all, delete-orphan")

class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    part_id = Column(Integer, ForeignKey("part.id"))
    part = relationship("Part", back_populates="question") 
    answer = relationship("Answer", back_populates="question", cascade="all, delete-orphan")

class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", back_populates="answer")

engine = create_engine('sqlite:///questions.db')
Base.metadata.create_all(bind=engine)