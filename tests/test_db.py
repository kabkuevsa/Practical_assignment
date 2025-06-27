import unittest
import os
from db import FormTemplateDB

class TestDB(unittest.TestCase):
    def setUp(self):
        """Создаём временную БД для тестов"""
        self.test_db = 'test_db.json'
        self.db = FormTemplateDB(self.test_db)
        
     
        self.db.add_template({
            "name": "Тестовая форма",
            "email": "email",
            "date": "date"
        })

    def tearDown(self):
        """Удаляем временную БД после тестов"""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_find_template(self):
        
        result = self.db.find_template({"email": "email", "date": "date"})
        self.assertEqual(result, "Тестовая форма")

       
        result = self.db.find_template({"nonexistent": "field"})
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()