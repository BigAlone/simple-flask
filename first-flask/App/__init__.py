from flask import Flask
from flask_cors import *

from App import settings
from App.ext import init_ext


def create_app(envname):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    # app.config['SECRET_KEY'] = "IAMHOLLY"
    app.config.from_object(settings.config.get(envname or 'default'))
    init_ext(app=app)
    from .main import main as main_blueprint
    app.register_blueprint(blueprint=main_blueprint, url_prefix='/')

    from App.auth import auth as auth_blueprint
    app.register_blueprint(blueprint=auth_blueprint, url_prefix='/auth')
    return app
