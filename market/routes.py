from market import app, db
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm

@app.route('/')
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route('/market')
def market_page():
    items = Item.query.filter(Item.Quantity >= 1).all()
    print(items)
    return render_template("market.html", items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    
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

    return render_template('register.html', form = form)