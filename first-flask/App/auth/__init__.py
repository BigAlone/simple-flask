# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: Holly
# @Date  : 2019-11-14
from flask import Blueprint

auth = Blueprint('auth', __name__)

from App.auth import views