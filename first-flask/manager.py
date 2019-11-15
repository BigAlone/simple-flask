from flask_migrate import MigrateCommand
from flask_script import Manager, Shell

from App import create_app
from App.ext import db
from App.model import Role, User

app = create_app("develop")
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command('shell', Shell(make_context=make_shell_context))


@manager.command
def test():
    import unittest
    testss = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(testss)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    manager.run()
