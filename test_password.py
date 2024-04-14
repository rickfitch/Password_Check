import unittest
from password_checker import validate_password

class TestPassword(unittest.TestCase):
    def test_validate_password(self):
        self.assertTrue(validate_password("Password1!"))
        self.assertFalse(validate_password("password1!"))
        self.assertFalse(validate_password("Password1"))
        self.assertFalse(validate_password("Password!"))
        self.assertFalse(validate_password("Password1"))
        self.assertFalse(validate_password("password1"))
        self.assertFalse(validate_password("password!"))
        self.assertFalse(validate_password("Password"))
        self.assertFalse(validate_password("password"))
        self.assertFalse(validate_password("12345678"))
        self.assertFalse(validate_password("!@#$%^&*"))
        self.assertFalse(validate_password("Password1"))
        self.assertFalse(validate_password("RickFitch123!"))
    
    if __name__ == '__main__':
        unittest.main()
        