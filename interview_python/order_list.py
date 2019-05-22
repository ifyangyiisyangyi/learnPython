"""
python 实现有序列表并列排名
"""

grade_list = [78, 75, 80, 89, 92, 93]
grade_list.sort(reverse=True)
print(grade_list)

for i in range(len(grade_list)):
    # print('成绩：{}'.format(grade_list[i]), ' 排名：{}'.format(i + 1))
    print(f'成绩:{grade_list[i]} 排名:{i+ 1}')   # format的简便写法


"""
情况一：有两个89并列第4，92应该是第5名， 解题思路：当出现第二次89时，排名不增加
成绩:75  排名: 1
成绩:78  排名: 2
成绩:80  排名: 3
成绩:89  排名: 4
成绩:89  排名: 4
成绩:92  排名: 5
成绩:93  排名: 6
"""
grade_list2 = [75, 78, 80, 89, 89, 92, 93]
current_index = 0
current_grade = 0
for grade in grade_list2:
    if grade > current_grade:
        current_index += 1
    print(f'成绩:{grade} 排名:{current_index}')
    current_grade = grade

"""
情况二：有两个89并列第4，92应该是第6名
成绩:75  排名: 1
成绩:78  排名: 2
成绩:80  排名: 3
成绩:89  排名: 4
成绩:89  排名: 4
成绩:92  排名: 6
成绩:93  排名: 7
"""
grade_list3 = [75, 78, 80, 89, 89, 92, 93]
current_grade = 0
current_index = 0
for index, grade in enumerate(grade_list3, start=1):
    if grade > current_grade:
        current_index = index
    print(f'成绩:{grade} 排名:{current_index}')
    current_grade = grade