from ovp_core import models
from rest_framework import serializers


class SkillSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ['name']
    model = models.Skill
