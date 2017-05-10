from ovp_core import validators
from ovp_core.models import Availability
from rest_framework import serializers


class AvailabilitySerializer(serializers.ModelSerializer):
  def validate(self, data):
    weekday, period = data.pop('weekday', 0), data.pop('period', 0)
    return {  'period_index': Availability.compose_period_index_for(weekday, period)  }
    # data['pk'] = Availability.compose_period_index_for(weekday, period)
    # return super().validate(data)

  class Meta:
    fields = ['weekday', 'period']
    model = Availability