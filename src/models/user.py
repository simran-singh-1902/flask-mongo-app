from mongoengine import Document
from werkzeug.security import generate_password_hash, check_password_hash
from mongoengine import StringField, DateTimeField
import logging
from mongoengine.connection import get_db


logger = logging.getLogger("default")

class User(Document):

  """
  TASK: Create a model for user with minimalistic
        information required for user authentication

  HINT: Do not store password as is.

  """
  username = StringField(required=True, unique=True)
  password_hash = StringField(required=True)

  def __str__(self):
    return self.username

  def verify_password(self, password):
    return check_password_hash(self.password_hash, password)

  def get_user_by_username(username):
    db = get_db()
    query = {'username': username}
    return db.user.find(query)
  
class Logs(Document):
  """
  Task that stores last login information in another collection of mongoDB
  """
  user_id = StringField(required=True)
  last_login = DateTimeField()

  def __str__(self):
    return self.user_id



