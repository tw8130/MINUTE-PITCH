import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    '''
    Test to test behaviour of user model class
    '''

    def setUp(self):
        '''
        Method that creates instance of user class and pass paswword property
        '''
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        '''
        Acsertains if password is being hashed  and if pass_secure contains a value
        '''
        self.assertTrue(self.new_user.pass_secure is not None)
    
    def test_no_access_password(self):
        '''
        Confirms if application raises an AttributeError when u try to access password property
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        '''
        Test that verifies password hash when we pass correct password
        '''
        self.assertTrue(self.new_user.verify_password('banana'))