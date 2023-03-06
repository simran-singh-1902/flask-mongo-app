import time
from celery import Celery
from celery.utils.log import get_task_logger
from mongoengine import get_db
from datetime import datetime

logger = get_task_logger(__name__)

try:
    capp = Celery('tasks',
                broker='amqp://admin:mypass@rabbit:5672',
                backend=get_db())
except Exception as e:
    print(str(e))


@capp.task()
def store_last_login(user_id):
    logger.info('Got Request - Starting work')
    time.sleep(4)
    db = get_db()
    query = {'user_id': user_id}
    last_login = datetime.utcnow()  
    update = {'$set': {'last_login': last_login}}
    logger.info("New Login by-> %s", user_id)  
    db.logs.update_one(query, update)
    logs = db.logs.find({'user_id': user_id})
    logger.info('Work Finished')
    for log in logs:
        return str(log['user_id'])+ "_" +str(log['_id'])