from datetime import datetime

from flask import request, jsonify, make_response, render_template, redirect, url_for, session, flash

from App.main import main
from App.main.Form import NameForm


@main.route('/', methods=["GET", "POST"])
def hello_world():
    current_time = datetime.utcnow()
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name')
        session['name'] = form.name.data
        return redirect(url_for('main.hello_world'))
    return render_template('index.html', form=form, name=session.get('name'))


@main.route('/index')
def index():
    headers = request.headers
    headers = dict(headers)
    return jsonify({"data": headers})


@main.route('/user')
def user():
    form = NameForm()
    return render_template('user.html', form=form)


@main.route('/set_cookie')
def cookies():
    response = make_response('<h1>This document carries a cookie</h1>')
    response.set_cookie('answer', "666")

    return response
