import csv
from datetime import datetime

from django.http import HttpResponse


def Response(rows, filename=None, sheet_name=None):
  if filename is None:
    filename = "data-export-{}.csv".format(datetime.now().strftime('%Y-%m-%d_%H%M%S'))
  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

  csv_writer = csv.writer(response)
  for row in rows:
    csv_writer.writerow(row)

  return response