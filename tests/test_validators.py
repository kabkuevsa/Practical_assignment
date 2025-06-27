import unittest
from validators import validate_email, validate_phone, validate_date

class TestValidators(unittest.TestCase):
    def test_email(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("invalid-email"))

    def test_phone(self):
        self.assertTrue(validate_phone("+7 123 456 78 90"))
        self.assertFalse(validate_phone("123456"))

    def test_date(self):
        self.assertTrue(validate_date("01.01.2025"))
        self.assertTrue(validate_date("2025-01-01"))
        self.assertFalse(validate_date("01/01/2025"))

if __name__ == '__main__':
    unittest.main()