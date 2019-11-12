# -*- coding: utf-8 -*-
# @File  : Form.py
# @Author: Holly
# @Date  : 2019-11-11

from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[Required()])
    submit = SubmitField('Submit')
