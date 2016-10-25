from django.test import TestCase

from ovp_core.models import GoogleAddress

class GoogleAddressModelTestCase(TestCase):
  def test_api_call(self):
    """Assert model calls google API and get address"""
    a = GoogleAddress(typed_address="Rua Teçaindá, 81, SP", typed_address2="Casa")
    a.save()

    a = GoogleAddress.objects.get(pk=a.pk)
    self.assertTrue(a.typed_address == "Rua Teçaindá, 81, SP")
    self.assertTrue(a.typed_address2 == "Casa")
    self.assertTrue(a.address_line == "Rua Teçaindá, 81, Pinheiros, São Paulo, SP, Brasil")
    self.assertTrue(a.lat)
    self.assertTrue(a.lng)
