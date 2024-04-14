#!/usr/bin/python3
"""
    This class inherits from Base and links to the MySQL table states.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql+mysqldb://username:password@localhost:3306/database_name?charset=latin1')

Base.metadata.create_all(engine)
