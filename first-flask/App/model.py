from App.ext import db


class Role(db.Model):
    __tablename__ = "first-roles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return f"<Role {self.name}>"


class User(db.Model):
    __tablename__ = "first-users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('first-roles.id'))

    def __repr__(self):
        return f"<User {self.username}>"
