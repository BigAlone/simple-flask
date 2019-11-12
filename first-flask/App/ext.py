# 配置第3方库-插件
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_moment import Moment
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
moment = Moment()


def init_ext(app):
    db.init_app(app)
    Session(app=app)
    bootstrap.init_app(app=app)
    moment.init_app(app=app)
    migrate.init_app(app=app, db=db)
