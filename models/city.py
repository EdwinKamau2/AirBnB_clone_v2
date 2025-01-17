#!/usr/bin/python3
""" Is the City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class City(BaseModel, Base):
    """ Is The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship('Place', backref="cities",
                            cascade="all, delete, delete-orphan")
    else:
        state_id = ""
        name = ""
