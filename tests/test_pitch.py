import unittest
from app.models import Pitch
from app import db



class TestPitch(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
 
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        # self.user = User(username = 'cliff', password = 'banana', email = 'cliff@gmail.com')
        self.new_pitch = Pitch(id=1, title="Pitch", body='pitches',category='Interview')


    def tearDown(self):

        Pitch.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))
    
    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,1)
        self.assertEquals(self.new_pitch.title,'Pitch')
        self.assertEquals(self.new_pitch.body,'pitches')
        self.assertEquals(self.new_pitch.category,"Interview")
        # self.assertEquals(self.new_pitch.writer,self.user)
    
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch()
        get_pitches = Pitch.get_pitch(1)
        self.assertTrue(len(get_pitches) == 1)
    

    
