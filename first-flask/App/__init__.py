from flask import Flask
from flask_cors import *

from App import settings
from App.ext import init_ext
from .main import main as main_blueprint


def create_app(envname):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    # app.config['SECRET_KEY'] = "IAMHOLLY"
    app.config.from_object(settings.config.get(envname or 'default'))
    init_ext(app=app)
    app.register_blueprint(blueprint=main_blueprint, url_prefix='/')
    return app
