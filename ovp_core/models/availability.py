from django.db import models
from django.utils.translation import ugettext_lazy as _


availability_periods = (
  (0, 'Manhã'),
  (1, 'Tarde'),
  (2, 'Noite')
)
availability_weekdays = (
  (0, 'Domingo'),
  (1, 'Segunda'),
  (2, 'Terça'),
  (3, 'Quarta'),
  (4, 'Quinta'),
  (5, 'Sexta'),
  (6, 'Sábado')
)

class Availability(models.Model):
  weekday = models.PositiveSmallIntegerField(_('Weekday'), choices=availability_weekdays, default=0)
  period = models.PositiveSmallIntegerField(_('Day period'), choices=availability_periods, default=0)
  period_index = models.PositiveSmallIntegerField(db_index=True)

  def save(self, *args, **kwargs):
    if self.pk is None:
      self.period_index = __class__.compose_period_index_for(self.weekday, self.period)

  def __str__(self):
    return "{} de {}".format(self.get_weekday_display(), self.get_period_display())

  @staticmethod
  def compose_period_index_for(weekday, period):
    return int(weekday) * len(availability_weekdays) + int(period)

  @staticmethod
  def decompose_period_index(index):
    weekday_count = len(availability_weekdays)
    return int(index / weekday_count), index % weekday_count