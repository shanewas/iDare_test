from time import sleep

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from celery import shared_task

channel_layer = get_channel_layer()


@shared_task
def my_task():
    for i in range(100):
        sleep(1)
        async_to_sync(channel_layer.group_send)(
            'tasks', {'type': 'send_percentage', 'text': f'{i}'})
