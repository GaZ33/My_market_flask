from flask_wtf import FlaskForm
from wtforms  import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

# Criando o forms para se registrar
class RegisterForm(FlaskForm):
    login = StringField(label="Username", validators=[Length(min=4, nax=15), DataRequired()])
    email_address = StringField(label="Email", validators=[Email(), DataRequired()])
    Fname = StringField(label="Primeiro nome", validators=[Length(min=3, max=15), DataRequired()])
    Mname = StringField(label="Nome do meio", validators=Length(min=3, max=25))
    Lname = StringField(label="Sobrenome", validators=[Length(min=3, max=15), DataRequired()])
    password1 = PasswordField(label="Senha", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirme sua senha", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Criar conta")

