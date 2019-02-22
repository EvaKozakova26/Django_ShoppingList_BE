import datetime

from rest_framework import serializers

from .models import Item, ShoppingList, MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'count', 'createdAt', 'state')

class ShoppingListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    user = UserSerializer(default=None)
    class Meta:
        model = ShoppingList
        fields = ('id', 'createdAt', 'user', 'items')
