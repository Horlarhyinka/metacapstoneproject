from django.test import TestCase
from restaurant.models import Booking, Menu

class MenuTest(TestCase):
    def test_get_menu(self):
        mod = Menu.objects.create(Title="test", Price=10.00, Inventory=10)
        self.assertEqual(mod, f"test: {str(10.00)}")