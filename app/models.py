from datetime import datetime

from django.db import models
from django.utils import timezone


class MyUser(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ShoppingList(models.Model):
    createdAt = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, default=None)


class Item(models.Model):
    name = models.CharField(max_length=50)
    createdAt = models.DateTimeField(default=datetime.now)
    count = models.IntegerField(default=1)
    state = models.BooleanField(default=False)
    shoppingList = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, null=True, default=None,
                                     related_name='items')

    def __str__(self):
        return self.name
