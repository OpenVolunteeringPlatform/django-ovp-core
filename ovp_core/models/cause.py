import vinaigrette
from django.db import models

class Cause(models.Model):
  name = models.CharField('name', max_length=100)

  def __str__(self):
    return self.name

  class Meta:
    app_label = 'ovp_core'
    verbose_name = 'cause'
    verbose_name_plural = 'causes'

vinaigrette.register(Cause, ['name'])
