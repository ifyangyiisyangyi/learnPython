from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import User


def hello(request):
    context = {}
    context['hello'] = 'hello nicolas junjie!'
    return render(request, 'hello.html', context)


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
