from . import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    todos = db.relationship('Todo')
    created_date = db.Column(db.Date, nullable=False,default=datetime.utcnow().date())
    updated_date = db.Column(db.Date, nullable=False,default=datetime.utcnow().date())

    
