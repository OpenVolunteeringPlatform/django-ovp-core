from ovp_core import models
from rest_framework import serializers


class CauseSerializer(serializers.ModelSerializer):
  name = serializers.CharField(required=False)

  class Meta:
    fields = ['id', 'name']
    model = models.Cause
