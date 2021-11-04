from __future__ import absolute_import, unicode_literals

from celery.decorators import task
from core.models import Record
from django.conf import settings
from django.http import HttpResponse
import requests
import json

URL = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=%s' % settings.AV_KEY

@task(name='fetch_and_store')
def fetch_and_store():
    rs = requests.get(URL)
    data = rs.json()
    exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    refresh_date = data['Realtime Currency Exchange Rate']['6. Last Refreshed']
    r = Record(price=exchange_rate, date=refresh_date)
    r.save()
    print('Fetch And Store Completed')
    return HttpResponse('API data fetched')
    