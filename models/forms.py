from wtforms import StringField, Form, StringField, BooleanField, PasswordField, validators, ValidationError, SubmitField, IntegerField, TextAreaField
from models import RegisterModel
from flask_wtf.file import FileRequired, FileAllowed, FileField
from flask_wtf import FlaskForm

class RegistrationForm(Form):
    name = StringField("Name", [validators.Length(min=3, max=40)])
    username = StringField("Username", [validators.Length(min=4, max=25)])
    email = StringField("Email", [validators.Length(min=6, max=64), validators.Email()])
    password = PasswordField("New Password", [
        validators.DataRequired(),
        validators.EqualTo('confirm', message="Passwords must match")
    ])
    confirm = PasswordField("Repeat Password")

class LoginForm(Form):
    email = StringField("Email", [validators.Length(min=6, max=64), validators.Email()])
    password = PasswordField("Password", [validators.DataRequired()])

class CustomerRegistrationForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    username = StringField('Username', [validators.DataRequired()])
    email = StringField("Email", validators=[validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message="Both passwords should match")])
    confirm = PasswordField("Repeat Password", [validators.DataRequired()])    
    country = StringField('Country', [validators.DataRequired()])
    state = StringField('State', [validators.DataRequired()])
    city = StringField('City', [validators.DataRequired()])
    contact = StringField('Contact', [validators.DataRequired()])
    address = StringField('Address', [validators.DataRequired()])

    profile_image = FileField("Profile Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'], "Images only")])
    
    submit = SubmitField("Register")

    def validate_username(self, username):
        if RegisterModel.query.filter_by(username=username.data).first():
            raise ValidationError("Username already Exists.")

    def validate_email(self, email):
        if RegisterModel.query.filter_by(email=email.data).first():
            raise ValidationError("Email already Exists.")

class CustomerLoginForm(FlaskForm):
    email = StringField("Email", validators=[validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

class AddProducts(Form):
    name = StringField("Name", [validators.DataRequired()])
    price = IntegerField("Price:RS ", [validators.DataRequired()])
    stock = IntegerField("Stock", [validators.DataRequired()])
    desc = TextAreaField("Description", [validators.DataRequired()])
    # colors = TextAreaField("Colors", [validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileAllowed(['jpg, jpeg, png, svg, gif']), 
                        "Images Only please"])