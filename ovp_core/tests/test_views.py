from django.test import TestCase

from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from ovp_core import models
from ovp_core import serializers

class TestStartupView(TestCase):
  def setUp(self):
    self.skills_data = serializers.SkillSerializer(models.Skill.objects.all(), many=True).data
    self.causes_data = serializers.CauseSerializer(models.Cause.objects.all(), many=True).data

  def test_returned_startup_data(self):
    """ Test startup route returns skills and causes """
    client = APIClient()
    response = client.get(reverse('startup'))

    self.assertTrue(response.status_code == 200)
    self.assertTrue(response.data['skills'] == self.skills_data)
    self.assertTrue(response.data['causes'] == self.causes_data)
