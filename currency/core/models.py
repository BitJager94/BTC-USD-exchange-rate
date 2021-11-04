from django.db import models


class Record(models.Model):

    price = models.TextField()

    date = models.DateTimeField()

