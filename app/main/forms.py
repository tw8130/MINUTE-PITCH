from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    pitch_title = StringField('Title', validators=[Required()])
    content = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('Advertisement','Advertisement Pitch'),('Project','Project Pitch'),('Interview','Interview Pitch'),('Promotion','Promotion Pitch'),('Pick-up lines','Pick-up lines Pitch')], validators=[Required()])
    submit = SubmitField('Write Pitch!')