from __future__ import absolute_import, unicode_literals
from celery import Celery
import os
from django.conf import settings


RABBIT_HOST = "amqp://guest:guest@%s:5672//" % os.environ.get('RABBIT_HOST')
CELERY_FREQ = os.environ.get('CELERY_FREQUENCY')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency.settings')

app = Celery('currency', broker=RABBIT_HOST)

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'fetch-every-1-hour': {
        'task': 'fetch_and_store',
        'schedule': int(CELERY_FREQ),
    },
}

