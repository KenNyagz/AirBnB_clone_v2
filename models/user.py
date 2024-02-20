#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ User class """
    __tablename__ = "users"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        #Define the relationship btwn places and user
        places = relationship("Place", cascade="all, delete-orphan", backref="user")
        #Creating a relationship between user and review
        reviews = relationship("Review", cascade="all, delete-orphan", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
