# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


availability_periods = [(0, 'Manhã'), (1, 'Tarde'), (2, 'Noite')]
availability_weekdays = [(0, 'Domingo'), (1, 'Segunda'), (2, 'Terça'), (3, 'Quarta'), (4, 'Quinta'), (5, 'Sexta'), (6, 'Sábado')]

def foward_func(apps, schema_editor):
    Availability = apps.get_model('ovp_core', 'Availability')
    for period in range(0, len(availability_periods)):
        for weekday in range(0, len(availability_weekdays)):
            index = weekday * len(availability_weekdays) + period
            Availability.objects.create(weekday=weekday, period=period, period_index=index)
    return True

def rewind_func(apps, schema_editor):
    Availability = apps.get_model('ovp_core', 'Availability')
    Availability.objects.all().delete()
    return True

class Migration(migrations.Migration):

    dependencies = [
        ('ovp_core', '0007_lead'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.PositiveSmallIntegerField(choices=availability_weekdays, default=0, verbose_name='Weekday')),
                ('period', models.PositiveSmallIntegerField(choices=availability_periods, default=0, verbose_name='Day period')),
                ('period_index', models.PositiveSmallIntegerField(db_index=True)),
            ],
        ),
        migrations.RunPython(foward_func, rewind_func)
    ]
