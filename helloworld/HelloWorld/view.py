from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import User
import random
import threading


def index(request):
    return render(request, '404.html')


def hello(request):
    data = User.objects.all()
    data1 = []
    for i in data:
        data1.append(i.user_name)
    return render(request, 'base.html', {'data': data1})


# 测试QQ号访问页面
def test_qq(request):
    '''请求页面'''
    return render(request, 'get_demo.html')


# 提交后返回页面
def result_qq(request):
    '''返回结果'''
    if request.method == 'GET':
        # 获取提交的数据
        r = request.GET["q"]  # key就是前面输入框里的name属性对应值name="q"
        return HttpResponse("测试结果：%s" % r)
    else:
        render(request, 'get_demo.html')


def user(request):
    '''请求页面-返回结果'''
    res = ""
    if request.method == 'GET':
        n = request.GET.get('name', None)  # key不存在时不会报错
        res = User.objects.filter(user_name="%s" % n)
        try:
            res = res[0].user_mail
        except:
            res = "未查询到数据"
        return render(request, 'get_email.html', {'email': res})
    else:
        return render(request, 'get_email.html', {'email': res})


def game(request):
    return render(request, 'game.html')


def gameResult(request):
    random_num = random.randint(0, 3)
    result = '...'
    '''返回结果'''
    if request.method == 'GET':
        # 获取提交的数据
        num = int(request.GET["number"])
        if num < random_num:
            result = 'too small'
            return render(request, 'game.html', {'result': result})
        elif num > random_num:
            result = 'too large'
            return render(request, 'game.html', {'result': result})
        else:
            result = 'bingo'
            return render(request, 'game.html', {'result': result})

