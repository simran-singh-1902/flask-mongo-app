import logging
from flask import request, jsonify
from services import UserService
from werkzeug.security import generate_password_hash, check_password_hash
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
        db.user.insert_one({"username":"Simran", "password_hash":generate_password_hash("123")})
        db.user.insert_one({"username":"Muskan", "password_hash":generate_password_hash("1234")})
        db.user.insert_one({"username":"Lakshya", "password_hash":generate_password_hash("1235")})
        logger.info("Added dummy data successfully!!")
        
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



