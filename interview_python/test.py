# 6  -3
# 10 -2
# 11 -2




# 1.请输入一串字符串，判断如果没有输入,提示：没有输入，程序结束；输入字符串后倒序输出，打印结果(5分)
# ① 输入字符串(2分)
# ② 倒叙输出并打印(3分)

def inputstring():
    while True:
        strcontent = input("请输入一串内容:")
        if strcontent == "":
            print("没有输入")
            return
        else:
            print(strcontent[::-1])


# 2、请输入第一个字符串，用户输入字符串后，回车结束，提示：请输入第二个字符串，用户输入字符串后，回车结束，进行逻辑判断，从第一字符串中删除第二字符串中的所有字符(5分)
# 例：第一个字符串输入：They are students ，第二个字符串输入"aeiou",第二个输入字符串中的字符存在于第一字符串中，则打印删除之后的第一个字符串变成"Thy e stdnts"
# ① 输入字符串(2分)
# ② 判断(2分)
# ③ 打印结果(1分)

def changestr():
    str1 = input("请输入第一个字符串1:")
    str2 = input("请输入第一个字符串2:")
    for i in str2:
        result = str1.replace(i, '')
        print(result)
        break
    for i in str2:
        result = result.replace(i, '')

    print(result)

# 3.使用字符串中的方法,统计字符串中大于1的字符和下标，并打印结果(5分)
# ① 统计大于1的字符(2分)
# ② 获取字符下标(2分)
# ③ 打印结果(1分)


def countnum():
    str1 = 'zhi cun gao yuan, wen ming qing shen, ye man ti po.'
    emptylis1 = []
    for i in str1:
        if i not in emptylis1 and i != ' ':
            emptylis1.append(i)
    for i in emptylis1:
        if str1.count(i) > 1:
            print("出现次数大于1的字符：%s, 次数：%d" % (i, str1.count(i)))
            for j in range(len(str1)):
                if str1[j] == i:
                    print("%s的下标有%d" % (i, j), end='   ')


# 4.打印1-30之间的所有3的倍数(5分)
# ① 判断(3分)
# ② 打印结果(2分)

def divthree():
    print("能被3整除的数:")
    for i in range(1, 31):
        if i % 3 == 0:
            print(i, end=' ')


# 5.编写冒泡排序(5分)
# ①使用嵌套循环(3分)
# ②打印排序后结果(2分)

def bulbsort(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j]<lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    print(lis)
    return lis

# 6.循环提示用户：输入用户名，密码，邮箱(要求用户输入的长度不超过20个字符(可以用切片)，如果超过打印输出)(15分)
#      用户名  密码    邮箱
#      admin    123456  tom@qq.com
#      只要在输入时，用户输入q或者Q，退出程序
# ① 输入(3分)
# 	② 判断(3分)
# ③ 使用切片(3分)
# ④ 循环(3分)
# ⑤ 打印结果(3分)

def inputpersoninfo():
    while True:
        str1 = input("请输入用户名，密码，邮箱，以空格隔开:")
        if str1 in ('q','Q'):
            print("退出系统")
            break
        else:
            if len(str1) > 20:
                print("超过了20个字符")
                continue
            else:
                try:
                    listr = str1.split(' ')
                    print("用户名:", listr[0])
                    print("密码:", listr[1])
                    print("邮箱:", listr[2])
                except:
                    print("请按格式输入三个数据")


# 7.将列表中“联想“和”微软”两个元素删除(注意越界)，并打印结果(5分)
# 例：list=["ph","leove","huawei","pad","神州","微软"]
# ①循环(2分)
# ② 判断(2分)
# ③ 打印结果(1分)

def lisremove():
    lis=["ph","leove","huawei","pad","神州","微软"]
    for item in ['联想', '微软']:
        try:
            lis.remove(item)
        except:
            print("数据不存在:", item)
    print(lis)


# 8.产生10个随机数,不能有重复的数据，将不重复的数据保存到列表中(考虑有重复数据的情况)(5分)
# ① 循环(2分)
# ② 判断重复数据(2分)
# ③ 打印結果(1分)

import random
def randomdata():
    lis = []
    while True:
        data = random.randint(1, 1000)
        if data not in lis:
            lis.append(data)
        if len(lis) == 10:
            print(lis)
            break

# 9.找出列表中的最大值，使用函数(10分)
# ① 函数定义(3分)
# ② 调用函数(2分)
# ③ 找出最大值(3分)
# ④ 打印结果(2分)

def maxdata(lis):
    maxdata = max(lis)
    print(maxdata)

# 10.使用匿名函数(结合 if else )，对列表中的奇数进行加1操作(5分)
# ① 使用匿名函数(2分)
# ② 判断(2分)
# ③ 打印结果(1分)

def addone():
    lis = [45,25,61,84,55,68,14]
    for i in lis:
        if i % 2 == 1:
            num = i + 1
            print(num, end=' ')


# 11.使用匿名函数，找出年龄大于20岁的学生(5分)
#  student=[
#          {'name':'tom','age':20},
#          {'name':'jack','age':18},
#          {'name':'lili','age':25},
#          {'name':'lucy','age':30}
#           ]
# ① 使用匿名函数(2分)
# ② 判断(2分)
# ③ 打印结果(1分)

def findstudent():
    student = [{'name':'tom','age':20},
              {'name':'jack','age':18},
              {'name':'lili','age':25},
              {'name':'lucy','age':30}]
    for item in student:
        if item.get('age') > 20:
            print("大于20岁的学生姓名:", item.get('name'))


# 12.给定两个list A，B，请找出A，B中相同的元素和不同的元素，分别打印相同和不同的元素(数据自己写)(5分)
# ① 找出相同元素(2分)
# ② 找出不同元素(2分)
# ③ 打印结果(1分)

def ABlis():
    lisA = [45,25,61,84,55,68,14]
    lisB = [45, 245, 62, 84, 53, 68, 14, 12, 'A', 'B', 'C']

    if len(lisA) > len(lisB):
        for i in lisA:
            if i not in lisB:
                print("不相同的数据:", i)
    else:
        for i in lisB:
            if i not in lisA:
                print("不相同的数据:", i)


# 13.现有字典d={‘a’=24,’b’=52,’c’=12,’d’=33}
# 请按字典中的value值进行降序排序，并按照顺序依次打印出来(5分)
# ① 循环(2分)
# ② 降序排序(2分)
# ③ 打印结果(1分)
def sortvalue():
    d = {'a':24,'b':52,'c':12,'d':33}
    lisvalue = d.values()
    lis = []
    for item in lisvalue:
        lis.append(item)
    lis.sort(reverse=True)
    print(lis)


# 14.编写一个用户注册功能  需要输入以下信息1.用户名 2.密码 3.确认密码4邮箱 5.手机号，6.自定义一个数据库列表(database)(20分)
# ① 输入数据(3分)
# ② 循环(5分)
# ③ 判断(5分)
# ④ 注册成功后将数据加入数据库(3)
# ⑤ 注册成功后是否需要继续注册(2分)
# ⑥ 打印结果(2分)


import pymysql


def insertdatatable():
    con = pymysql.connect(user='root', password='123456', db='exma', charset='utf8')
    cour = con.cursor()
    cour.execute('drop table if exists studentinfo')
    cour.execute('create table studentinfo (name varchar(20),password varchar(20),surepw varchar(20),email varchar(20),phone varchar(20))')
    while True:
        name = input("姓名:")
        password = input("密码:")
        surepw = input("确认密码:")
        email = input("email:")
        phone = input("phone:")

        cour.execute("insert into studentinfo values('%s', '%s', '%s', '%s', '%s')" % (name, password, surepw, email, phone))
        con.commit()
        cour.execute('select * from studentinfo')
        print(cour.fetchall())
        s = input("是否还要注册账号 是 或 否：")
        if s == '否':
            break
    cour.close()
    con.close()





if __name__ == '__main__':
    changestr()