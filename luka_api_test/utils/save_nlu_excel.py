import xlwt


def save_nlu_data():
    book = xlwt.Workbook()
    sheet = book.add_sheet('nlu_report')
    sheet.write(0, 0, label = 'Row 0, Column 0 Value')
    book.save('luka_api_test/report/nlu_report.xlsx')



