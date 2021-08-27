import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iDare_project.settings')


app = Celery('iDare_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.beat_schedule = {
    
# }

app.autodiscover_tasks()