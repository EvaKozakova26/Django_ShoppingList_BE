from django.db import models

# Create your models here.

class Item(models.Model):
    itemName = models.CharField(max_length=50)
    date = models.DateTimeField('date published')


class Type(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    typeName = models.CharField(max_length=20);
