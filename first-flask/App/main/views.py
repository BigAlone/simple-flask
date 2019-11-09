from flask import request, jsonify, make_response, render_template

from App.main import main


@main.route('/')
def hello_world():
    return 'Hello World!', 200


@main.route('/index')
def index():
    headers = request.headers
    headers = dict(headers)
    return jsonify({"data": headers})


@main.route('/set_cookie')
def cookies():
    response = make_response('<h1>This document carries a cookie</h1>')
    response.set_cookie('answer', "666")

    return response
