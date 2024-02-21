#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = ''
    id = Column(String(60), nullable=False, primary_key=True)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(128), nullable=False)
        #id = Column(String(60), nullable=False, primary_key=True)
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """returns the list of City instances with state_id equals to the
               current State.id;the FileStorage relationship btn State and City"""
            from models import storage
            list_cities = []
            for city in storage.all(City).value():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
