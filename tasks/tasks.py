from time import sleep

from celery import shared_task

@shared_task
def task():
    sleep(1)
    return