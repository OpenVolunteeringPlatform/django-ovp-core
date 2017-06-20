from ovp_core import models
from rest_framework import serializers

class SimpleAddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.SimpleAddress
    fields = ['street', 'number', 'neighbourhood', 'city', 'state', 'zipcode', 'country', 'supplement']
