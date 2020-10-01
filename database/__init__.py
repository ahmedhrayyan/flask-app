from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, String, Integer, Binary, Text, DateTime
from datetime import datetime
import bcrypt

db = SQLAlchemy()


def init_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()

# MODELS


ENCODING = 'utf-8'


class User(db.Model):
    __tablename__ = 'users'
    username = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(Binary, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())

    def __init__(self, name: str, username: str, password: str):
        self.name = name
        self.username = username
        self.password = bcrypt.hashpw(
            bytes(password, ENCODING), bcrypt.gensalt(12))

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def checkpw(self, password: str):
        if bcrypt.checkpw(bytes(password, ENCODING), self.password):
            return True
        return False

    def format(self):
        return {
            "id": self.id,
            "name": self.name
        }
