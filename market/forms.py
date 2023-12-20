from flask_wtf import FlaskForm
from wtforms  import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class RegisterForm(FlaskForm):
    login = StringField(label="Username", validators=[Length(min=4, nax=15), DataRequired])
    email_address = StringField(label="Email", validators=[Email(), DataRequired])
    Fname = StringField()
    Mname = StringField()
    Lname = StringField
    password1 = PasswordField()

