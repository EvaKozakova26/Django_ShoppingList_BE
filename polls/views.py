from django.http import HttpResponse
from django.template import loader

from polls.models import Item


def index(request):
    latest_items_list = Item.objects.order_by('-date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_items_list': latest_items_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, item_id):
    return HttpResponse("You are looking at item %s." % item_id)
