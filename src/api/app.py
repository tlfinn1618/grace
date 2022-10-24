import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'gracebase.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    membership_type = db.Column(db.String)
    users_info = db.relationship('UserInfo', backref='user')

    def __repr__(self):
        return f'<User "{self.first_name + " " + self.last_name}"'


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    address = db.Column(db.String)
    address_line_two = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    zip = db.Column(db.String)
    phone = db.Column(db.String)

    def __repr__(self):
        return f'<UserInfo "{self.user_id}">'


class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    date = db.Column(db.Date)

    def __repr__(self) -> str:
        return f'<Newsletter "{self.title}">'


class Bulletin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    date = db.Column(db.Date)

    def __repr__(self) -> str:
        return f'<Bulletin "{self.title}">'
