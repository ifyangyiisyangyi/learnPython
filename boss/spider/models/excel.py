# -*- coding:utf-8 -*-


import xlwt


fields = ['category', 'company', 'job',
          'location', 'experience', 'education',
          'salary', 'hr', 'description']


def save_as_xlsx(data):
    if len(data) == 0:
        return
    book = xlwt.Workbook()
    sheet = book.add_sheet(data[0].category)
    for i in range(len(fields)):
        sheet.write(0, i, fields[i])
    for index, value in enumerate(data):
        for i in range(len(fields)):
            value = dict(value)
            sheet.write(index+1, i, value[fields[i]])
    book.save('./xlsx/boss.xlsx')





