from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fake User'}
    posts = [
        {
            'author': {'username': 'jpants'},
            'body': 'who even are these people?'
        },
        {
            'author': {'username': 'notabot'},
            'body': 'these are not robots'
        },
        {
            'author': {'username': 'skeptic_system'},
            'body': 'I\'m not so sure about that'
        },
        {
            'author': {'username': 'notabot'},
            'body': '@skeptic_system is an idiot'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
