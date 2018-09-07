from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import IndexView

urlpatterns = [
    # ex: /polls/
    #    path('', views.index, name='index'),
    # ex: /polls/5/
    # Add Django site authentication urls (for login, logout, password management)
    #  path('', include('django.contrib.auth.urls')),

    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^auth/$', views.login_form, name='login_form'),
    url(r'^$', IndexView.as_view(), name="index"),

    path('<int:pk>/', views.DetailsView.as_view(), name='detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
