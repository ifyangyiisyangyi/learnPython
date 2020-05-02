# -*-coding: UTF-8 -*-

from django.http import HttpResponse

from TestModel.models import Test
from TestModel.models import Person,User

# 数据库操作

def testdb(request):
    # test1 = Test(name='w3cschool.cn')
    # test1.save()
    # return HttpResponse("<p>数据添加成功!</p>")
    test1 = Person(name = 'yy', age = '32')
    test1.save()
    return HttpResponse('person表插入数据成功')

def add_user(request):
    test1 = User(user_name = 'yy', user_pwd = '123456a', user_mail = '117645743@qq.com')
    test2 = User(user_name = 'yy', user_pwd = '123456a', user_mail = '117645743@qq.com')
    test1.save()
    test2.save()
    return HttpResponse("用户创建成功，快去看看吧")
