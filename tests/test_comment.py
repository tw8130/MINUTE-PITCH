import unittest
from app.models import User,Comment
from app import db


class TestComment(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Comment class
    '''


    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.user = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_comment = Comment(comment_content = 'comment', pitch_id = 1, user_id=self.user)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
      

    def test_instance(self):
        '''
        test case that uses the isinstance() to check if object is an instance of Comment class
        '''
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        '''
        test that uses self.assertEqual to check for the expected  comment results
        '''
        self.assertEquals(self.new_comment.pitch_id,1)
        self.assertEquals(self.new_comment.comment_content,'comment')
        self.assertEquals(self.new_comment.user_id,self.user)
     
    def test_save_comment(self):
        '''
        test that calls save_comment() method to save our comment objects
        '''
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
    
    def test_get_comments_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(1)
        self.assertTrue(len(got_comments) == 1)