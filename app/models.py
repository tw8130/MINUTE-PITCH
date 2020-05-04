from . import db
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    '''
    User class to create new users
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    '''
    Role class to create roles for our users
    '''
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

class Pitch(db.Model):
    __tablename__= 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String())
    body = db.Column(db.String())
    category = db.Column(db.String())
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    writer = db.Column(db.Integer,db.ForeignKey("users.id"))


# class Comment(db.Model):
#     __tablename__='comments'

#     id = db.Column(db.Integer,primary_key=True)
#     comment_content = db.Column(db.String())
#     pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
#     user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
