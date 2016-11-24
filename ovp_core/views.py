from rest_framework import response
from rest_framework import decorators

from ovp_core import models
from ovp_core import serializers

@decorators.api_view(['GET'])
def startup(request):
  """ This view provides initial data to the client, such as available skills and causes """
  skills = serializers.SkillSerializer(models.Skill.objects.all(), many=True)
  causes = serializers.CauseSerializer(models.Cause.objects.all(), many=True)

  return response.Response({
    'skills': skills.data,
    'causes': causes.data
  })
