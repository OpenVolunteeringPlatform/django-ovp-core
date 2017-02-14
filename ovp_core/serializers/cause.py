from ovp_core import models
from rest_framework import serializers


class CauseSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ['id', 'name']
    model = models.Cause
