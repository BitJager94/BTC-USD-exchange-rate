FROM python:3.8.3-slim

ENV PYTHONUNBUFFERED 1

COPY ./currency /currency

WORKDIR /currency
EXPOSE 8000

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && python -m pip install --upgrade pip \
    && pip install Django \
    && pip install psycopg2 \
    && pip install celery \
    && pip install requests \
    && pip install python-dotenv




