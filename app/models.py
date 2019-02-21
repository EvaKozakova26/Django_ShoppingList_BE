import datetime

from django.db import models
from django.utils import timezone


class ShoppingList(models.Model):
    createdAt = models.DateTimeField('date created')


class Item(models.Model):
    name = models.CharField(max_length=50)
    createdAt = models.DateTimeField('date created')
    count = models.IntegerField
    state = models.BooleanField
    shoppingList = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
