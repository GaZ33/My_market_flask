from market import app, db, LoginManager
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm
from flask_login import login_user, login_required, logout_user

@app.route('/', methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home_page():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        attempted_user = User.query.filter_by(Login=login_form.login.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=login_form.password.data):
            login_user(attempted_user)
            flash(f"Sucesso! Você está logado como {attempted_user.Login}", category="success")
            redirect(url_for('market_page'))
        else:
            flash(f'Usuário ou senha estão incorretos, por favor tente novamente!', category="danger")
    return render_template("home.html", login_form=login_form)

@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    items = Item.query.filter(Item.Quantity >= 1).all()
    login_form = LoginForm()
    purchase_form = PurchaseItemForm()
    if login_form.validate_on_submit:
        attempted_user = User.query.filter_by(Login=login_form.login.data).first()
        if attempted_user and attempted_user.check_password_correction(login_form.password.data):
            login_user(attempted_user)
            redirect(url_for('market_page'))
    return render_template("market.html", items=items, login_form=login_form, purchase_form=purchase_form)

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
    if login_form.validate_on_submit():
        attempted_user = User.query.filter_by(Login = login_form.login.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password = login_form.password.data):
            login_user(attempted_user)
            flash(f"Sucesso! Você está logado como {attempted_user.Login}", category="sucess")
            redirect(url_for('market_page'))
        else:
            flash(f'Usuário ou senha estão incorretos, por favor tente novamente!', category="danger")
    return render_template('register.html', form = form, login_form=login_form)

@app.route('/logout')
def logout_page():
    logout_user()
    return redirect(url_for('home_page'))