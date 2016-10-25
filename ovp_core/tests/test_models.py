from django.test import TestCase

from ovp_core.models import GoogleAddress
from ovp_core.models import AddressComponent
from ovp_core.models import AddressComponentType

class GoogleAddressModelTestCase(TestCase):
  def test_api_call(self):
    """Assert GoogleAddress calls google API and get address"""
    a = GoogleAddress(typed_address="Rua Teçaindá, 81, SP", typed_address2="Casa")
    a.save()

    a = GoogleAddress.objects.get(pk=a.pk)
    self.assertTrue(a.typed_address == "Rua Teçaindá, 81, SP")
    self.assertTrue(a.typed_address2 == "Casa")
    self.assertTrue(a.address_line == "Rua Teçaindá, 81, Pinheiros, São Paulo, SP, Brasil")
    self.assertTrue(a.__str__() == "Rua Teçaindá, 81, Pinheiros, São Paulo, SP, Brasil")
    self.assertTrue(a.lat)
    self.assertTrue(a.lng)

    a.address_line=None
    self.assertTrue(a.__str__() == "")

class AddressComponentTypeModelTestCase(TestCase):
  def test_str_call(self):
    """Assert AddressComponentType __str__ returns name"""
    a = AddressComponentType(name="xyz")
    a.save()

    self.assertTrue(a.__str__() == "xyz")

class AddressComponentModelTestCase(TestCase):
  def test_str_call(self):
    """Assert AddressComponent __str__ returns long name"""
    a = AddressComponent(short_name="short", long_name="long")
    a.save()

    self.assertTrue(a.__str__() == "long")
