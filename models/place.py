#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
        reviews = relationship('Review', backref='place',
                               cascade='delete')
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False,
                                 back_populates='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """returns the list of Review instances with
            place_id equals to the current Place.id
            """
            review_list = []
            rev_list = models.storage.all(Review).values()
            for revs in rev_list:
                if revs.place_id == self.id:
                    review_list.append(revs)
            return review_list

        @property
        def amenities(self):
            """returns the list of Amenities instances with
            Place.amenities
            """
            amenities_list = []
            rev_list = models.storage.all(Amenities).values()
            for revs in rev_list:
                if revs.place_id == self.id:
                    amenities_list.append(revs)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            """...
            """
            if obj.__class__.__name__ == 'Amenity':
                amenity_ids.append(obj.id)
