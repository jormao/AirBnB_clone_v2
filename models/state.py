#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    elif getenv('HBNB_TYPE_STORAGE') == 'file':
        name = ''

        @property
        def cities(self):
            """Return a list of City instance
            """
            city_list = []
            for _id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
