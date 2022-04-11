from django.shortcuts import render
import xlwt

from django.http import HttpResponse
from client.views import Client




def export_client_xls(request):
    """Funcion para generar reporte  de clientes"""

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="client.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Client')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Nombre', 'Descripcion',]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Client.objects.all().values_list('name', 'description')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response