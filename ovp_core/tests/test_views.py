from django.test import TestCase
from django.core import mail

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
    response = client.get(reverse("startup"), format="json")

    self.assertTrue(response.status_code == 200)
    self.assertTrue(response.data["skills"] == self.skills_data)
    self.assertTrue(response.data["causes"] == self.causes_data)


class TestContactFormView(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.basis_data = {"name": "my-name", "message": "my message", "email": "reply_to@asddsa.com"}

  def test_cant_send_invalid_recipient(self):
    """ Test sending contact form to invalid recipient does not work """
    data = self.basis_data

    data["recipients"] = ["invalid@recipient.com"]
    response = self.client.post(reverse("contact"), data=data, format="json")
    self.assertTrue(response.status_code == 400)
    self.assertTrue(response.data["detail"] == "Invalid recipients.")
    self.assertTrue(len(mail.outbox) == 0)

    data["recipients"] = ["testemail@1.com", "invalid@recipient.com"]
    response = self.client.post(reverse("contact"), data=data, format="json")
    self.assertTrue(response.status_code == 400)
    self.assertTrue(response.data["detail"] == "Invalid recipients.")
    self.assertTrue(len(mail.outbox) == 0)

  def test_can_send_valid_recipient(self):
    """ Test sending contact form to valid recipient does work """
    data = self.basis_data
    data["recipients"] = ["testemail@1.com"]

    response = self.client.post(reverse("contact"), data=data, format="json")
    self.assertTrue(response.status_code == 200)
    self.assertTrue(len(mail.outbox) == 1)
    self.assertTrue(data["name"] in mail.outbox[0].body)
    self.assertTrue(data["message"] in mail.outbox[0].body)
    self.assertTrue(data["email"] in mail.outbox[0].body)

  def test_can_send_multiple_valid_recipients(self):
    """ Test sending contact form to multiple valid recipient does work """
    data = self.basis_data
    data["recipients"] = ["testemail@1.com", "testemail@2.com"]

    response = self.client.post(reverse("contact"), data=data, format="json")
    self.assertTrue(response.status_code == 200)
    self.assertTrue(len(mail.outbox) == 2)
