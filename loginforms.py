from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, SubmitField, EmailField, StringField, TextAreaField
from wtforms.validators import InputRequired, Email, EqualTo, Length

# define our own FlaskForm subclass for our form
class RegisterForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", 
        validators=[InputRequired(), Length(min=8, max=256)])
    confirm_password = PasswordField("Confirm Password", 
        validators=[EqualTo('password')])
    username = StringField("Username", validators=[InputRequired()])
    bio = TextAreaField("Bio", validators=[Length(max = 50)])
    submit = SubmitField("Register")

# define our own FlaskForm subclass for our form
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", 
        validators=[InputRequired(), Length(min=8, max=256)])
    submit = SubmitField("Login")
