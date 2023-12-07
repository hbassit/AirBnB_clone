#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):

    def test_initialization(self):
        base_obj = BaseModel()
        self.assertIsInstance(base_obj, BaseModel)
        self.assertIsInstance(base_obj.id, str)
        self.assertIsInstance(base_obj.created_at, datetime)
        self.assertIsInstance(base_obj.updated_at, datetime)

    def test_save(self):
        base_obj = BaseModel()
        check1 = base_obj.updated_at
        time.sleep(1)
        base_obj.save()
        self.assertNotEqual(check1, base_obj.updated_at)

    def test_str(self):
        base_obj = BaseModel()
        s = f"[{type(base_obj).__name__}] ({base_obj.id}) {base_obj.__dict__}"
        self.assertEqual(base_obj.__str__(), s)

    def test_dict(self):
        base_obj = BaseModel()
        dic = base_obj.to_dict()
        self.assertIsInstance(dic, dict)
        self.assertIn('id', dic.keys())
        self.assertIn('created_at', dic.keys())
        self.assertIn('updated_at', dic.keys())
        self.assertEqual(dic['__class__'], type(base_obj).__name__)


if __name__ == "__main__":
    unittest.main()
