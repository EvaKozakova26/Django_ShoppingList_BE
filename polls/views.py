from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

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


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

#
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        #         # Return an 'invalid login' error message.
        ...


def logout_view(request):
    logout(request)
    # Redirect to a success page.
