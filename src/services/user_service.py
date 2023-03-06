from models import User, Logs
from mongoengine.connection import get_db
import logging

logger = logging.getLogger("default")

class UserService(object):
    """
    service function for user related business logic
    """

    def login_user(username, password):
        """
        TASKS: write the logic here for user login
               authenticate user credentials as per your
               schema and return the identifier user.

               raise appropriate errors wherever necessary
        """
        user = User.get_user_by_username(username)
        for user in user:
            print(user)
            verrified = User(user['first_name'], user['last_name'],user['email'], user['username'], user['password_hash'], user['created_on']).verify_password(password)
            if user and verrified:
                print(verrified)
                return str(user['username'])+ "_" +str(user['_id'])
        else:
            raise ValueError('Invalid username or password')
    

    
