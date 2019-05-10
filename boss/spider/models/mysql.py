# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('mysql+pymysql://root:root123@localhost:3306/boss?charset=utf8')


Session = sessionmaker(bind=engine)


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String(64), nullable=False)
    company = Column(String(64), nullable=False)
    job = Column(String(64), nullable=False)
    location = Column(String(64), nullable=False)
    experience = Column(String(64), nullable=False)
    education = Column(String(64), nullable=False)
    salary = Column(String(64), nullable=False)
    hr = Column(String(64), nullable=False)
    description = Column(Text, nullable=False)


def init_db():
    Base.metadata.create_all(engine)


def save_into_database(data):
    session = Session()
    for value in data:
        session.add(Job(category=value.category,
                    company=value.company,
                    job=value.job,
                    location=value.location,
                    experience=value.experience,
                    education=value.education,
                    salary=value.salary,
                    hr=value.hr,
                    description=value.description))
    session.commit()
