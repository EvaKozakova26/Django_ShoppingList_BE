import dateutil.parser
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, request, JsonResponse
from django.shortcuts import render, redirect
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import logging

from first_django import settings
from app.models import Item, ShoppingList
from app.serializer import ItemSerializer, ShoppingListSerializer


class ItemsView(APIView):
    serializer_class = ItemSerializer

    def post(self, request):
        shopList = request.data
        items = shopList['items']
        return Response(items, status=status.HTTP_201_CREATED)



class CreateItem(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateItem(APIView):
    def put(self, request):
        itemDict = request.data
        itemId = itemDict['id']
        item = Item.objects.get(id=itemId)
        item.state = itemDict['state']
        item.save()

        return Response(request.data, status=status.HTTP_201_CREATED)


class DeleteItem(APIView):
    def delete(self, request):
        itemDict = request.data
        itemId = itemDict['id']
        item = Item.objects.get(id=itemId)
        item.delete()
        return Response(request.data, status=status.HTTP_201_CREATED)


class CreateShoppingList(APIView):
    def post(self, request, *args, **kwargs):
        newShopList = ShoppingList.objects.create()
        itemList = request.data
        for it in itemList:
            print(it)
            itemId = it['id']
            item = Item.objects.get(id=itemId)
            item.shoppingList = newShopList
            item.save()

        return Response("", status=status.HTTP_201_CREATED)


class UpdateShoppingList(APIView):
    def post(self, request):
        shoppingListDto = request.data
        items = shoppingListDto['items']
        shoppingListDict = shoppingListDto['shoppingList']
        sListId = shoppingListDict['id']
        shoppingList = ShoppingList.objects.get(id=sListId)
        for it in items:
            itemId = it['id']
            item = Item.objects.get(id=itemId)
            item.shoppingList = shoppingList
            item.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

class ShoppingListsView(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer



def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            login(request, user)
            return redirect('/app/')


def logout_view(request):
    logout(request)
    return redirect('/app/')
