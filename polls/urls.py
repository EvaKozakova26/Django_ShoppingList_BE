from django.urls import path, include

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    # Add Django site authentication urls (for login, logout, password management)
    path('', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index"),

    path('<int:pk>/', views.DetailsView.as_view()),

]
