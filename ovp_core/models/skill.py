import vinaigrette
from django.db import models

class Skill(models.Model):
  name = models.CharField('name', max_length=100)

  def __str__(self):
    return self.name

  class Meta:
    app_label = 'ovp_core'
    verbose_name = 'skill'

vinaigrette.register(Skill, ['name'])
