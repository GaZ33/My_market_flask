from market import app, db, LoginManager
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from flask_login import login_user, login_required

@app.route('/', methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home_page():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        attempted_user = User.query.filter_by(Login=login_form.login.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=login_form.password.data):
            login_user(attempted_user)
            flash(f"Sucesso! Você está logado como {attempted_user.Login}", category="sucess")
        else:
            flash(f'Usuário ou senha estão incorretos, por favor tente novamente!', category="danger")
    return render_template("home.html", login_form=login_form)

@app.route('/market')
@login_required
def market_page():
    items = Item.query.filter(Item.Quantity >= 1).all()
    print(items)
    return render_template("market.html", items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    login_form = LoginForm()
    if form.validate_on_submit():
        user_creted = User(Login=form.login.data, 
                    Email=form.email_address.data, 
                    password=form.password1.data,
                    FName=form.Fname.data, 
                    MName=form.Mname.data, 
                    LName=form.Lname.data)
        db.session.add(user_creted)
        db.session.commit()
        return redirect(url_for("market_page"))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"Houve um erro ao criar a conta: {err_msg[0]}", category="danger")
            print(type(err_msg))

    return render_template('register.html', form = form, login_form=login_form)