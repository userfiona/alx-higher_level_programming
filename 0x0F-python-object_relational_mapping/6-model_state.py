#!/usr/bin/python3
"""
This script defines the State class and creates an instance of Base.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of Base
Base = declarative_base()

# Define the State class
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
