#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db', "Should be work in db")
class TestDbStorage(unittest.TestCase):
    '''this will test the DbStorage'''

    def testState(self):
        state = State(name="Antioquia")
        if state.id in models.storage.all():
            self.asserTrue(state.name, "Antioquia")

if __name__ == "__main__":
    unittest.main()
