import logging
from flask import request, jsonify
from services import UserService
from werkzeug.security import generate_password_hash
from mongoengine.connection import get_db
from celery import Celery
from datetime import datetime

try:
    capp = Celery('worker',
                broker='amqp://admin:mypass@rabbit:5672',
                backend=get_db())
except Exception  as e:
    print(str(e))

logger = logging.getLogger("default")


def index():
    logger.info("Checking the flask scaffolding logger")
    return "Welcome to the flask scaffolding application"

def dummy_data():
    try:
        db = get_db()
        db.user.insert_many([
            {"first_name":"Simran", "last_name":"Singh", "email":"Simran@gmail.com", "username":"Simran", "password_hash":generate_password_hash("123"), 'created_on': datetime.utcnow()},
            {"first_name":"Muskan", "last_name":"Sharma", "email":"Muskan@gmail.com", "username":"Muskan", "password_hash":generate_password_hash("1234"), 'created_on': datetime.utcnow()},
            {"first_name":"Lakshya", "last_name":"Verma", "email":"Lakshya@gmail.com", "username":"Lakshya", "password_hash":generate_password_hash("1235"), 'created_on': datetime.utcnow()}
        ])
        logger.info("Added dummy data successfully!!")
        return jsonify({'status': 'Added dummy users successfully!!'}), 200
        
    except Exception as e:
        return jsonify({'error exception': str(e)}), 500

def create_user():
    """
    creates a new user, if not already exists
    """
    try:
        db = get_db()
        username = request.json['username']
        password = request.json['password']
        first_name = request.json.get('first_name', '')
        last_name = request.json.get('last_name', '')
        email = request.json.get('email')        
        created_on = datetime.utcnow()

        if db.user.find_one({'username': username}):
            return jsonify({'status': 'User already exist'}), 401
        db.user.insert_one({"first_name": first_name, "last_name":last_name, "email": email,"username":username, "password_hash":generate_password_hash(password), "created_on": created_on})
        return jsonify({'status': 'New user created successfully'}), 200

    except Exception as e:
        return jsonify({'error exception': str(e)}), 500


def get_users():
    """
    lists all the existing users!!
    """
    try:
        db = get_db()
        print(db.user.find())
        users = db.user.find()
        data = []
        for user in users:
            print(user)
            data.append({'name': user['first_name']+ " " +user['last_name'],'email': user['email'], 'created on': user['created_on']})
        return jsonify(data), 200

    except Exception as e:
        return jsonify({'error exception': str(e)}), 500

def login():
    """
    TASKS: write the logic here to parse a json request
           and send the parsed parameters to the appropriate service.

           return a json response and an appropriate status code.
    """
    try:
        username = request.json['username']
        password = request.json['password']
        user_id = UserService.login_user(username, password)
        print("**** Got user_id ***", user_id)
        #capp.send_task('tasks.store_last_login', kwargs={'user_id': user_id})
        return jsonify({'user_id': user_id, 'status': 'Login Successfull !!'}), 200
    except ValueError as e:
        return jsonify({'Value-error': str(e)}), 401
    except Exception as e:
        return jsonify({'error exception': str(e)}), 500



