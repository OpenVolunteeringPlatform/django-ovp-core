from ovp_core import models
from rest_framework import serializers


class CauseSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ['name']
    model = models.Cause
