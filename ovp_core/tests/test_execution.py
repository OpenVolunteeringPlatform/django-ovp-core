from django.test import TestCase
from rest_framework.test import APIRequestFactory

from ovp_core.schemas import OVPSchemaGenerator

# Just import to test execution
from ovp_core import apps
from ovp_core import urls

class TestSchemaGenerator(TestCase):
  def test_schema_generation(self):
    """Assert that OVPSchemaGenerator executes without raising exceptions"""
    factory = APIRequestFactory()
    request = factory.post('/')

    generator = OVPSchemaGenerator()
    schema = generator.get_schema(request=request)
