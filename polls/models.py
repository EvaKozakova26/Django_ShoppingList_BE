import datetime

from django.db import models
from django.utils import timezone


class Item(models.Model):
    itemName = models.CharField(max_length=50)
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.itemName

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)


class Type(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    typeName = models.CharField(max_length=20);

    def __str__(self):
        return self.typeName
