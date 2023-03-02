from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a Form Class:
class FormEntryName(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit_button = SubmitField('Submit') 
