#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        # Many-to-many relationship between place and amenity
        place_amenities = relationship("Place", secondary='place_amenity')

        # Association table for the Many-To-Many relationship between Place and Amenity tables
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                              Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

    else:
        name = ""
