from ovp_core import models
from rest_framework import serializers


class SkillSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ['id', 'name']
    model = models.Skill
