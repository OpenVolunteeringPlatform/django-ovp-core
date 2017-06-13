from django.db import models

class SimpleAddress(models.Model):
  street = models.CharField(max_length=300, null=True, blank=True)
  number = models.CharField(max_length=10, null=True, blank=True) # May contain letters as well
  neighbourhood = models.CharField(max_length=100, null=True, blank=True)
  city = models.CharField(max_length=100, null=True, blank=True)
  state = models.CharField(max_length=100, null=True, blank=True)
  zipcode = models.CharField(max_length=20, null=True, blank=True)
  country = models.CharField(max_length=100, null=True, blank=True)
