from django.urls import path, include

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:item_id>/', views.detail, name='detail'),
    # Add Django site authentication urls (for login, logout, password management)
    path('', include('django.contrib.auth.urls')),

]
