from time import sleep
import logging
import os

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

@celery.task(name="create_task", serializer='json')
def create_task():
    logging.warning("waiting")
    sleep(10)
    logging.warning("comp")
    return "hello"