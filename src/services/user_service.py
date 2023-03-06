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
            if user and User(user['username'], user['password_hash']).verify_password(password):
                return str(user['username'])+ "_" +str(user['_id'])
        else:
            raise ValueError('Invalid username or password')
    

    
