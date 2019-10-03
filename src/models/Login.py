from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, nom):
        self.nom = nom

    def __repr__(self):
        return '<User %r>' % self.nom

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

