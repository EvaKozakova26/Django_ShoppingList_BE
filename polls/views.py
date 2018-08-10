from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from polls.models import Item


def index(request):
    latest_items_list = Item.objects.order_by('-date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_items_list': latest_items_list,
    }
    return HttpResponse(template.render(context, request))


# get_obj.. metoda, ktera bere model a klicove slovo a zobrazi item, kdyz existuje, jinak raise 404
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'polls/detail.html', {'item': item})  # vraci HTTPRquest..
