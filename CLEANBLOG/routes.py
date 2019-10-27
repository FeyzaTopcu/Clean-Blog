from flask import render_template, flash, redirect, url_for
from CLEANBLOG import app
from CLEANBLOG.forms import RegisterForm,LoginForm


@app.route('/')
def index():
    return render_template('index.html', title ="HOME" )

@app.route('/about')
def about():
    return render_template('about.html', title="ABOUT")

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if( form.validate_on_submit()):
        flash(f'{form.name.data} account created', 'access')
        return redirect(url_for('index'))
    return render_template('register.html', title='REGISTER', form=form)


@app.route('/login', methods= ['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'fyztpc@gmail.com':
            flash(f'Logged in succesfully','success')
            return redirect(url_for('index'))
    return render_template('login.html', title= 'LOGIN', form=form)