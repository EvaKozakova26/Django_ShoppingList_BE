from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from first_django import settings
from polls.models import Item
from polls.serializer import ItemSerializer


class IndexView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'polls/index.html'

    def get(self, request):
        queryset = Item.objects.all()
        return Response({'items': queryset})

    def perform_create(self, serializer):
        """Save the post data when creating a new items."""
        serializer.save()


class DetailsView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    login_url = '/polls/login/'
    redirect_field_name = ''

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

#

def login_form(request):
    return render(request, 'registration/login.html', {})

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        # the password verified for the user
        if user.is_active:
            login(request, user)
            return redirect('/polls/')
    else:
        return render(request, 'registration/login.html', {})

def logout_view(request):
    logout(request)
    return redirect('/polls/')
