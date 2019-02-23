from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import ItemsView

urlpatterns = [
    # ex: /app/
    #    path('', views.index, name='index'),
    # ex: /app/5/
    # Add Django site authentication urls (for login, logout, password management)
    #  path('', include('django.contrib.auth.urls')),

    url(r'^$', ItemsView.as_view(), name="index"),

    path('api/getItems', views.ItemsView.as_view()),
    path('api/getLists/', views.ShoppingListsView.as_view()),
    path('api/new', views.CreateItem.as_view()),
    path('api/saveList', views.CreateShoppingList.as_view()),
    path('api/check', views.UpdateItem.as_view()),
    path('api/delete', views.DeleteItem.as_view()),
    path('api/updateList', views.UpdateShoppingList.as_view()),
    path('api/deleteList', views.DeleteList.as_view()),

    path('api/register', views.CreateNewUser.as_view()),
    path('api/loginn', views.LoginUser.as_view()),
    path('api/logoutt', views.LogoutUser.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
