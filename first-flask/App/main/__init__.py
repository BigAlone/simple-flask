# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: Holly
# @Date  : 2019-08-28

from flask import Blueprint

main = Blueprint('main', __name__)

from App.main import views
