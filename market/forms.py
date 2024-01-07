from flask_wtf import FlaskForm
from wtforms  import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

# Criando o forms para se registrar
class RegisterForm(FlaskForm):

    def validate_login(self, login_check):
        login = User.query.filter_by(Login=login_check.data).first()
        if login:
            raise ValidationError("Já existe o usuário inserido! por favor tente um diferente")
        
    def validate_email_address(self, email_check):
        login = User.query.filter_by(Email=email_check.data).first()
        if login:
            raise ValidationError("Já existe o email inserido! por favor tente um diferente")

    # Utilizamos validators para criar algumas restrições e/ou checar o campo
    login = StringField(label="Usuário", validators=[Length(min=4, max=15), DataRequired()])
    email_address = StringField(label="Email", validators=[Email(), DataRequired()])
    Fname = StringField(label="Primeiro nome", validators=[Length(min=3, max=15), DataRequired()])
    Mname = StringField(label="Nome do meio", validators=[Length(min=3, max=25)])
    Lname = StringField(label="Sobrenome", validators=[Length(min=3, max=15), DataRequired()])
    password1 = PasswordField(label="Senha", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label="Confirme sua senha", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Criar conta")

class LoginForm(FlaskForm):
    login = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Senha", validators=[])
    submit = SubmitField(label="Entrar")