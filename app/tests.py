from django.test import TestCase

# Create your tests here.
from datetime import datetime

from django.test import TestCase

from app.models import Item


class ItemTestCase(TestCase):

    def setUp(self):
        self.item = Item.objects.create(name='TestName', createdAt=datetime.now(), shoppingList_id="", state=False)

    def testGetItems(self):
        self.assertEquals(Item.objects.get(name='TestName').name, 'TestName')
