from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from polls.models import Item


def index(request):
    latest_items_list = Item.objects.order_by('-date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_items_list': latest_items_list,
    }
    return HttpResponse(template.render(context, request))


# get_obj.. metoda, ktera bere model a klicove slovo a zobrazi item, kdyz existuje, jinak raise 404
@login_required(login_url='/polls/login/')
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.user.is_authenticated:
        print("loggged")
    else:
        print("not logged madafaka")
    return render(request, 'polls/detail.html', {'item': item})  # vraci HTTPRquest..
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
