import dateutil.parser
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, request, JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import logging

from app.auth import CsrfExemptSessionAuthentication
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
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CreateShoppingList, self).dispatch(request, *args, **kwargs)

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        currentUser = request.user
        newShopList = ShoppingList.objects.create()
        newShopList.user = currentUser
        newShopList.save()
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


class DeleteList(APIView):
    def delete(self, request):
        listDict = request.data
        listId = listDict['id']
        list = ShoppingList.objects.get(id=listId)
        list.delete()
        return Response(request.data, status=status.HTTP_201_CREATED)


class ShoppingListsView(generics.ListCreateAPIView):
    serializer_class = ShoppingListSerializer
    authentication_classes = (BasicAuthentication, SessionAuthentication)
    permission_classes = (AllowAny,)

    def get_queryset(self):
        user = self.request.user
        if user.is_active:
            return ShoppingList.objects.filter(user=user)
        return ShoppingList.objects.all()



class CreateNewUser(APIView):
    def post(self, request):
        userData = request.data
        name = userData['name']
        passwrd = userData['password']
        User.objects.create_user(username=name, password=passwrd)
        return Response(request.data, status=status.HTTP_201_CREATED)


class LoginUser(APIView):
    def post(self, request):
        userData = request.data
        name = userData['name']
        passwrd = userData['password']
        user = authenticate(username=name, password=passwrd)
        if user is not None:
            if user.is_active:
                login(request, user)
                print(" im logged madafakas")
                return Response(request.data, status=status.HTTP_201_CREATED)


class LogoutUser(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)

    def get(self, request):
        print(self.request.user)
        print("logout")
        logout(request)
        return Response(self.request.data, status=status.HTTP_201_CREATED)
