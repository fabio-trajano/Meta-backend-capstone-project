from django.test import TestCase
from .models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice Cream", price=3, inventory=100)
        self.assertEqual(item, "Ice Cream : 3")
