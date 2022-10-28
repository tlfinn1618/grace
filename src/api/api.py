from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
from flask_marshmallow import Marshmallow
import requests
import os

Base = declarative_base()

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'gracebase.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey=("User.id"))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    user_title = db.Column(db.String(30))
    email = db.Column(db.String(255))
    mobile = db.Column(db.String(10))

    def __init__(self, first_name, last_name, user_title, email, mobile):
        self.first_name = first_name
        self.last_name = last_name
        self.user_title = user_title
        self.email = email
        self.mobile = mobile


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    text = db.Column(db.String)
    date = db.Column(db.Date)

    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date


class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'password')


class UserInfoSchema(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'user_title', 'email', 'mobile')


class NewsSchema(ma.Schema):
    class Meta:
        fields = ('title', 'text', 'date')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

user_info_schema = UserInfoSchema()

news_schema = NewsSchema()
all_news_schema = NewsSchema(many=True)

# Endpoint to create a new user


@app.route('/user', methods=["POST"])
def add_user():
    username = request.json['username']
    password = request.json['password']
    new_user = User(username, password)
    db.session.add(new_user)
    db.session.commit()

    user = User.query.get(new_user.id)

    return user_schema.jsonify(user)

# Endpoint to query all users


@app.route("/users", methods=["GET"])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

# Endpoint to querying a single user


@app.route("/user/<id>", methods=["GET"])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# Endpoint to updating a single user

@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    password = request.json['password']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    user_title = request.json['user_title']
    email = request.json['email']
    mobile = request.json['mobile']

    user.username = username
    user.password = password
    user.first_name = first_name
    user.last_name = last_name
    user.user_title = user_title
    user.email = email
    user.mobile = mobile

    db.session.commit()
    return user_schema.jsonify(user)


# Endpoint to deleting a single user

@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return "You have successfully deleted this user"


if __name__ == '__main__':
    app.run(debug=True)
