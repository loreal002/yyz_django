from django.test import TestCase
from .models import  Event,Guest

# Create your tests here.

class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=2000,
        address='shenzhen', start_time='2016-08-31 02:18:22')

        Guest.objects.create(id=1,event_id=1,realname='alen',
        phone='13711001101',email='alen@mail.com', sign=False)

    def test_event_models(self):
        result = Event.objects.get(name='oneplus 3 event')
        self.assertEqual(result.address,'beijing')
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(realname='alen')
        self.assertEqual(result.phone,'13711001101')
        self.assertFalse(result.sign)
