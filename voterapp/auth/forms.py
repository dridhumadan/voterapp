from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, EqualTo
from voterapp.auth.utils import CL


class RegistrationForm(FlaskForm):
    email_id = StringField('Email ID', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators = [DataRequired()])
    last_name = StringField('Last Name', validators = [DataRequired()])
    dob = DateField('Date of Birth', validators = [DataRequired()])
    address = TextAreaField('Address', validators = [DataRequired()])
    constituency = SelectField('Constituency', choices = CL.con_list, validators = [DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email_id = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Login')
