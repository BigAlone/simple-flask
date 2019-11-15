from flask import make_response, render_template, redirect, url_for, session
from flask_login import login_required

from App.ext import db
from App.main import main
from App.main.Form import NameForm
from App.model import User


@main.route('/', methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


@main.route('/user')
def user():
    form = NameForm()
    return render_template('user.html', form=form)


@main.route('/set_cookie')
def cookies():
    response = make_response('<h1>This document carries a cookie</h1>')
    response.set_cookie('answer', "666")

    return response


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.route('/secret')
@login_required
def secret():
    return "Only authenticated user are allowed!"
