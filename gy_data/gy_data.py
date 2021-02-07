"""
gy数据处理
"""
import xlwt
from openpyxl import Workbook

# 字段声明
data_time = []
lx = []
ly = []
rx = []
ry = []
extra = []


def get_data():
    '''
    抽取数据
    :return: 数据时间，5组有效数据
    '''
    with open('1万次右摇杆上归中值') as file:
        data = file.readlines()
        if data[0] == '\n':
            data.remove(data[0])
        for i in data:
            data_item = i.strip()  # 去掉换行符
            data_item_list = data_item.split(',')  # 行数据用逗号分割成list
            data_time.append((data_item_list[0]))
            lx.append(data_item_list[1])  # lx列表
            ly.append(data_item_list[2])
            rx.append(data_item_list[3])
            ry.append(data_item_list[4])
            extra.append(data_item_list[5])
    return data_time, lx, ly, rx, ry, extra


# def save_data():
#     '''
#     保存数据
#     :return: 数据保存excel
#     '''
#     fields = ['RX1万次左极限值', 'RX2万次左极限值', 'RX3万次左极限值']
#     data_time, lx, ly, rx, ry, extra = get_data()
#     write_book = xlwt.Workbook(encoding='utf-8')
#     sheet = write_book.add_sheet("摇杆数据分析", cell_overwrite_ok=True)
#     for i in range(len(fields)):
#         sheet.write(0, i, fields[i])
#     for a in range(len(lx)):
#         sheet.write(a + 1, 0, lx[a])
#     for b in range(len(ly)):
#         sheet.write(b + 1, 1, ly[b])
#     for c in range(len(rx)):
#         sheet.write(c + 1, 2, rx[c])
#     write_book.save('RX1万次左极限值.xlsx')


if __name__ == '__main__':
    # save_data()
    pass
