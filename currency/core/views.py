from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from core.tasks import fetch_and_store
from core.models import Record

import requests
import json

KEY = settings.API_KEY
URL = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=%s' % settings.AV_KEY


def index(req):
    data = { 'key' : KEY}
    return render(req, 'index.html', context=data)


def exchange_rate(req):
    try:
        e_rate = Record.objects.last().price
        return HttpResponse('Exchange Rate = %s' % e_rate)
    except:
        return HttpResponse('No Record Available In DB')


@csrf_exempt
def manual_fetch(req): #couldn't run celery task using fetch_and_store.delay()
    rs = requests.get(URL)
    data = rs.json()
    exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    refresh_date = data['Realtime Currency Exchange Rate']['6. Last Refreshed']
    r = Record(price=exchange_rate, date=refresh_date)
    r.save()
    return HttpResponse('API data fetched')
    

