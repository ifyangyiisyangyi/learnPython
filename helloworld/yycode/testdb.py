# -*-coding: UTF-8 -*-

from django.http import HttpResponse
from TestModel.models import User


# 数据库操作

def add_user(request):
    test1 = User(user_name='yy', user_pwd='123456a', user_mail='117645743@qq.com')
    test1.save()
    return HttpResponse("用户创建成功，快去看看吧")
