from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from polls.models import Item


def index(request):
    latest_items_list = Item.objects.order_by('-date')[:20]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_items_list': latest_items_list,
    }
    return HttpResponse(template.render(context, request))


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
