from io import BytesIO
from datetime import datetime

from pyexcel_xls import save_data

from django.http import HttpResponse


def Response(rows, filename=None,sheet_name="root"):
  if filename is None:
    filename = "data-export-{}.xls".format(datetime.now().strftime('%Y-%m-%d_%H%M%S'))

  xls_buffer = BytesIO()
  save_data(xls_buffer, {str(sheet_name): rows})

  response = HttpResponse(xls_buffer.getvalue(), content_type='application/vnd.ms-excel')
  response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)

  return response