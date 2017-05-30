from ovp_core import validators
from ovp_core.models import Availability
from rest_framework import serializers


class AvailabilitySerializer(serializers.ModelSerializer):
  def to_representation(self, instance):
    return { 'weekday': instance.weekday, 'period': instance.period }

  def validate(self, data):
    if not 'period_index' in data:
      data['period_index'] = Availability.compose_period_index_for(data.get('weekday', 0), data.get('period', 0))
    return super().validate(data)

  class Meta:
    fields = ['weekday', 'period']
    model = Availability

