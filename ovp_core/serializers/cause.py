from ovp_core import models
from ovp_core import validators
from rest_framework import serializers
from ovp_uploads.serializers import UploadedImageSerializer

class FullCauseSerializer(serializers.ModelSerializer):
  image = UploadedImageSerializer()
  class Meta:
    fields = ['id', 'name', 'image']
    model = models.Cause

class CauseSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ['id', 'name']
		model = models.Cause

class CauseAssociationSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField()
  name = serializers.CharField(read_only=True)

  class Meta:
    fields = ['id', 'name']
    model = models.Cause
    validators = [validators.cause_exist]
