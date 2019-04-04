from datetime import datetime

from django.test import TestCase

from app.models import Item


class ItemTestCase(TestCase):

    def setUp(self):
        self.item = Item.objects.create(itemName='TestName', date=datetime.now())

    def testGetItems(self):
        self.assertEquals(Item.objects.get(itemName='TestName').itemName, 'TestName')
