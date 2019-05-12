# -*- coding:utf-8 -*-


import xlwt
import time

fields = ['category', 'company', 'job',
          'location', 'experience', 'education',
          'salary', 'hr', 'description']


def save_as_xlsx(data):
    if len(data) == 0:
        return
    book = xlwt.Workbook() # 创建Workbook对象
    sheet = book.add_sheet(data[0].category) # 增加一个sheet页, xlwt.Worksheet.Worksheet对象
    for i in range(len(fields)): 
        sheet.write(0, i, fields[i]) # 第一行依次写入岗位信息
    for index, value in enumerate(data):
        for i in range(len(fields)):
            value = dict(value)
            sheet.write(index+1, i, value[fields[i]])
    # book.save('./xlsx/boss.xlsx')
    time_current = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    book.save('./xlsx/' + time_current + 'boss.xlsx')





