#!/usr/bin/python
"""Unittests for DBStorage class of AirBnb_Clone_v2"""
import unittest
import pep8
import os
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import MySQLdb


@unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') != 'db',
        "This test only work in DBStorage")
class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    @classmethod
    def setUpClass(cls):
        """Tests"""
        cls.dbstorage = DBStorage()
        cls.output = StringIO()
        sys.stdout = cls.output

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.dbstorage
        del cls.output

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_new(self):
        """test when new is created"""
        obj = State(name="California")
        self.assertEqual(obj.name, "California")

    def test_new_user(self):
        """test new user"""
        new_user = User(email="mail@mail.com", password="mail")
        self.assertTrue(new_user.email, "mail@mail.com")

    def test_method(self):
        """method exist"""
        self.assertTrue(hasattr(self.dbstorage, "all"))
        self.assertTrue(hasattr(self.dbstorage, "new"))
        self.assertTrue(hasattr(self.dbstorage, "save"))
        self.assertTrue(hasattr(self.dbstorage, "delete"))

    def test_all(self):
        """check all"""
        storage.reload()
        obj = storage.all()
        self.assertisInstance(obj, dict)
        self.assertEqual(len(obj), 0)
        new = User(email="mail@mail.com", password="mail")
        console = self.create()
        console.onecmd("create State name=California")
        result = storage.all("State")
        self.assertTrue(len(obj) > 0)

    def test_storage(self):
        """ test storage is an instance"""
        self.assertTrue(isinstance(storage.DBStorage))

if __name__ == "__main__":
    unittest.main()
