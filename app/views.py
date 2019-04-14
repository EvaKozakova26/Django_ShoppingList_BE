from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app.auth import CsrfExemptSessionAuthentication
from app.models import Item, ShoppingList
from app.serializer import ItemSerializer, ShoppingListSerializer


class ItemsView(APIView):
    serializer_class = ItemSerializer

    def post(self, request):
        shop_list = request.data
        items = shop_list['items']
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
        item_dict = request.data
        item_id = item_dict['id']
        item = Item.objects.get(id=item_id)
        item.state = item_dict['state']
        item.save()

        return Response(request.data, status=status.HTTP_201_CREATED)


class DeleteItem(APIView):
    def delete(self, request):
        item_dict = request.data
        item_id = item_dict['id']
        item = Item.objects.get(id=item_id)
        item.delete()
        return Response(request.data, status=status.HTTP_201_CREATED)


class CreateShoppingList(APIView):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CreateShoppingList, self).dispatch(request, *args, **kwargs)

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        current_user = request.user
        new_shop_list = ShoppingList.objects.create()
        new_shop_list.user = current_user
        new_shop_list.save()
        item_list = request.data
        for it in item_list:
            print(it)
            item_id = it['id']
            item = Item.objects.get(id=item_id)
            item.shoppingList = new_shop_list
            item.save()
        return Response("", status=status.HTTP_201_CREATED)


class UpdateShoppingList(APIView):
    def post(self, request):
        shopping_list_dto = request.data
        items = shopping_list_dto['items']
        shopping_list_dict = shopping_list_dto['shoppingList']
        s_list_id = shopping_list_dict['id']
        shopping_list = ShoppingList.objects.get(id=s_list_id)
        for it in items:
            item_id = it['id']
            item = Item.objects.get(id=item_id)
            item.shoppingList = shopping_list
            item.save()
        return Response(request.data, status=status.HTTP_201_CREATED)


class DeleteList(APIView):
    def delete(self, request):
        list_dict = request.data
        list_id = list_dict['id']
        list = ShoppingList.objects.get(id=list_id)
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
        return ShoppingList.objects.filter(id=999999)  # temporary workaround


class CreateNewUser(APIView):
    def post(self, request):
        user_data = request.data
        name = user_data['name']
        passwrd = user_data['password']
        User.objects.create_user(username=name, password=passwrd)
        return Response(request.data, status=status.HTTP_201_CREATED)


class LoginUser(APIView):
    def post(self, request):
        user_data = request.data
        name = user_data['name']
        passwrd = user_data['password']
        user = authenticate(username=name, password=passwrd)
        if user is not None:
            if user.is_active:
                login(request, user)
                print("user is logged in")
                return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_204_NO_CONTENT)


class LogoutUser(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)

    def get(self, request):
        print(self.request.user)
        print("logout")
        logout(request)
        return Response(self.request.data, status=status.HTTP_201_CREATED)
