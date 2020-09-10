
import requests
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Message, Blog, Vistor, spider_article
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def show_404(request):
    return render(request, '404.html')


def login(request):
    ip = get_user_ip(request)
    # url = 'http://ip.ws.126.net/ipquery?ip=223.10.136.26'
    url = f"http://www.ip-api.com/json/{ip}?lang=zh-CN"
    user_agent = ""
    country = ""
    city = ""
    ip_as = ""
    isp = ""
    if ip == '127.0.0.1':
        print("本地请求")
    else:
        try:
            res = requests.get(url)
            ip_message = res.json()
            if "HTTP_USER_AGENT" in request.META:
                user_agent = request.META['HTTP_USER_AGENT']
            else:
                user_agent = ""

            if ip_message.get('status') == 'success':
                country = ip_message.get('country')
                city = ip_message.get('city')
                ip_as = ip_message.get('as')
                isp = ip_message.get('isp')
            elif ip_message.get('status') == 'fail':
                print("请求失败")
            else:
                pass
        except:
            print("获取ip信息异常")
        try:
            visitor = Vistor(ip=ip, user_agent=user_agent, country=country, city=city, ip_as=ip_as, isp=isp)
            visitor.save()
            # send_mail(f'访问者IP:{ip}', f'访问者地址:{city}', '117645743@qq.com', ['937471204@qq.com'])
        except:
            print("写入数据异常")
    try:
        blog_info = model_to_dict(Blog.objects.get(id=1))
        print(blog_info)
    except:
        blog_info = {'id': 1, 'blog_date': '2020-08-10', 'blog_title': '点我跳转至github', 'blog_content': "test"}
    try:
        count = Vistor.objects.filter().count()
    except:
        count = "数据异常"
    return render(request, 'index.html', {'blog_info': blog_info, 'count': count})


def get_user_ip(request):
    """
    获取访问用户ip
    :param request:
    :return:
    """
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        return request.META['HTTP_X_FORWARDED_FOR']
    else:
        return request.META['REMOTE_ADDR']


def save_message(request):
    '''
    发送联系人信息后回到主页
    :param request:
    :return: 返回主页
    '''
    ip = get_user_ip(request)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get('email')
        message = request.POST.get('message')

        test1 = Message(ip=ip,
                        name=name,
                        email=email,
                        message=message
                        )
        try:
            test1.save()
        except:
            print("保存数据异常")
    return HttpResponseRedirect('/')


def article_show(request):
    """
    :param request:
    :return: 分页显示文章内容
    """
    article_obj = spider_article.objects.all()  # 获取文章表里所有数据
    article_list = []
    for i in article_obj:
        article_list.append(i)
    paginator = Paginator(article_list, 20)  # 实例化Paginator，每页显示10条数据
    if request.method == "GET":
        page = request.GET.get('page')  # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        try:
            articles = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            articles = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            articles = paginator.page(paginator.num_pages)

    return render(request, 'article_show.html', {'articles': articles})


