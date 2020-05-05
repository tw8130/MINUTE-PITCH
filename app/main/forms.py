from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,SelectField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    pitch_title = StringField('Title', validators=[Required()])
    content = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('Advertisement','Advertisement Pitch'),('Project','Project Pitch'),('Interview','Interview Pitch'),('Promotion','Promotion Pitch'),('Pick-up lines','Pick-up lines Pitch')], validators=[Required()])
    submit = SubmitField('Write Pitch!')

class CommentForm(FlaskForm):
    comment_content = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField('Comment')

class GeneralForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')

class GeneralReviewForm(FlaskForm):
    review = StringField('Review:',validators=[Required()])
    submit = SubmitField('Submit')

class ProjectForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')

class ProjectReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')

class AdvertisementForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')

class AdvertisementReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')

class SaleForm(FlaskForm):
    post = StringField('Title', validators=[Required()])
    body = TextAreaField('Post', validators=[Required()])
    submit = SubmitField('Submit')


class SaleReviewForm(FlaskForm):
    review = StringField('Review: ', validators=[Required()])
    submit = SubmitField('Submit')

