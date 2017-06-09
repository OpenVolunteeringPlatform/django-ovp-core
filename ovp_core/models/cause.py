import vinaigrette
from django.db import models

from django.utils.translation import ugettext_lazy as _

class Cause(models.Model):
  name = models.CharField('name', max_length=100)
  image = models.ForeignKey('ovp_uploads.UploadedImage', blank=True, null=True, verbose_name=_('image'))
  
  def __str__(self):
    return self.name

  class Meta:
    app_label = 'ovp_core'
    verbose_name = _('cause')

vinaigrette.register(Cause, ['name'])
