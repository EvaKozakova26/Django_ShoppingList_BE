import datetime

from rest_framework import serializers

from .models import Item, ShoppingList


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'count', 'createdAt', 'state')

class ShoppingListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = ShoppingList
        fields = ('id', 'createdAt', 'items')
