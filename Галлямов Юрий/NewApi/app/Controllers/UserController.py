import json

from app.Model.UserModel import User
# from app.controllers import *
from app.Model.database import *
from flask import request, Blueprint, jsonify
import datetime

from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

user_bp = Blueprint('User', __name__)
@user_bp.route('/users', methods=["GET"])
def get_users():
    users = User.query.all()
    user_data = []

    for user in users:
        user_info = {
            "login": user.Login_User,
            "fio": user.FIO_User,
            "avatar": user.Avatar_User,
            "status": user.Status_User,
            "role": user.Role
        }
        user_data.append(user_info)

    return jsonify({"users": user_data})

@user_bp.route('/registration/', methods=['POST'])
def registration():
    data_json = request.json
    login = data_json['login']
    password = data_json['password']
    name = data_json['name']
    avatar = data_json.get('avatar','')

    if (login and password and name) is None:
        return jsonify({
            "code": 400,
            "message": "Missing required parameters"
        })

    try:
        user = User(login, password, name, avatar, False, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), 0)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            "code": 200,
            "message": "Registration succeed"
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "code": 400,
            "message": "login already available"
        })

@user_bp.route('/login', methods=['POST'])
def auth_login():
    data_json = request.json
    login = data_json['login']
    password = data_json['password']
    print("NEn")
    user = User.query.filter(User.Login_User == login and User.Password == password).first()

    print(f"{user} log - {login} and pass - {password}")

    if user is None:
        return jsonify({"code": 405, "message": "Login is error"})
    print(f"log {user.Login_User}")
    # login_user(user)
    return jsonify({"code": 200,
                    "message": "Login is succsed",
                    "result": [{
                        "login": user.Login_User,
                        "password": user.Password,
                        "name": user.FIO_User,
                        "avatar": user.Avatar_User,
                        "status": user.Status_User,
                    }]
                })


@user_bp.route('/user', methods=['GET'])
def get_user():
    login = request.args.get('login')

    if login is None:
        return jsonify({
            "code": 500,
            "message": "An error occurred on the server while sending profile"
        })

    user = db.session.query(User).get(login)

    if user is None:
        return jsonify({
            "code": 500,
            "message": "Login not found"
        })

    return jsonify({
        "code": 200,
        "result": [
            {
                "login": user.Login_User,
                "fio": user.FIO_User,
                "avatar": user.Avatar_User,
                "status": user.Status_User,
                "role": user.Role
            }
        ]
    })

@user_bp.route('/user', methods=['GET'])
def user_edit():

    data_json = request.json
    login = data_json['login']
    password = data_json['password']
    name = data_json['name']
    avatar = data_json.get('avatar', '')

    user = db.session.query(User).get(login)

    if user is None:
        return jsonify({
            'code': 500,
            'message': "An error occurred on the server while edit profile"
        })

    try:

        user.password = password
        user.name = name
        user.avatar = avatar

        db.session.commit()

        return jsonify({
            "code":200,
            "message": "profile is edit"
        })

    except:
        db.session.rollback()
        return jsonify({
            'code': 500,
            'message': "An error occurred on the server while edit profile"
        })


@user_bp.route('/searchContacts', methods=['GET'])
def search_user():

    name = request.args.get('contacts')

    contacts = (db.session.query(User).filter(User.FIO_User.like(f"%{name}%"))).all()

    contacts_data = []
    for contacts in contacts:
        user_info = {
            "login": contacts.Login_User,
            "fio": contacts.FIO_User,
            "avatar": contacts.Avatar_User,
            "status": contacts.Status_User,
            "role": contacts.Role
        }
        contacts_data.append(user_info)

    return jsonify({"users": contacts_data})

