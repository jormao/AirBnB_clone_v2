#!/usr/bin/python3
"""New engine DBStorage"""
import json
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

all_classes = {"State", "City"}


class DBStorage:
    """Save in the database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine to the database.
        """
        var_eng = "{0}+{1}://{2}:{3}@{4}:3306/{5}".format(
            'mysql', 'mysqldb', getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'), getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB'))
        self.__engine = create_engine(var_eng, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary with all classes.
        """
        entities = dict()
        if cls:
            return self.get_data_from_table(cls, entities)
        for entity in all_classes:
            entities = self.get_data_from_table(entity, entities)
        self.__session.close()
        return entities

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables into database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def get_data_from_table(self, cls, structure):
        """returns data for the to_all class method.
        """
        if type(structure) is dict:
            query = self.__session.query(eval(cls))
            for _row in query.all():
                key = "{}.{}".format(_row.__class__.__name__, _row.id)
                structure[key] = _row
            return structure
