from ovp_core import models

from rest_framework import serializers

class EmptySerializer(serializers.Serializer):
  class Meta:
    fields = []

class GoogleAddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.GoogleAddress
    fields = ['typed_address', 'typed_address2', 'address_line', 'city_state']
    read_only_fields = ['address_line', 'city_state']

class GoogleAddressLatLngSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.GoogleAddress
    fields = ['typed_address', 'typed_address2', 'address_line', 'city_state', 'lat', 'lng']
    read_only_fields = ['address_line', 'city_state']

class GoogleAddressCityStateSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.GoogleAddress
    fields = ['city_state']

class SkillSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ['name']
    model = models.Skill

class CauseSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ['name']
    model = models.Cause
