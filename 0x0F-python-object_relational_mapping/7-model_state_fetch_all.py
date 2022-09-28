#!/usr/bin/python3
"""Script that lists all State objects from the database
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sessionmaker
from model_state import Base, State

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
session = sessionmaker()
for instance in session.query(State):
    print(instance.name, instanace.fullname)
