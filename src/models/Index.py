from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Activite(db.Model):
    __tablename__ = 'activite'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, nom):
        self.nom = nom

    def __repr__(self):
        return '<Activite %r>' % self.nom

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

