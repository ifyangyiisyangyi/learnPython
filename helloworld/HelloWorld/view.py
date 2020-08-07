import requests
from bs4 import BeautifulSoup
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import User, Message, Blog, Article, Vistor


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
        visitor = Vistor(ip=ip, user_agent=user_agent, country=country, city=city, ip_as=ip_as, isp=isp)
        try:
            visitor.save()
        except:
            print("写入数据异常")
    try:
        blog_info = model_to_dict(Blog.objects.get(id=1))
        print(blog_info)
    except:
        blog_info = {'id': 1, 'blog_title': '点我跳转至github', 'blog_content': "test"}
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
    ip = get_user_ip(request)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get('email')
        message = request.POST.get('message')

        test1 = Message(ip = ip,
                        name=name,
                        email=email,
                        message=message
                        )
        try:
            test1.save()
        except:
            print("message save exception")
    return render(request, 'index.html')


def get_article_page(url):
    r = requests.request('get', url=url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    ls = soup('h3', class_="com-article-panel-title")
    url_dict = {}
    for tag in ls:
        s = 'https://cloud.tencent.com' + tag.a['href']
        title = tag.a.string
        article = Article(title=title,
                          linkage=s,
                          tag="python")
        article.save()
        url_dict[title] = s  # 返回文章的标题和链接
    return url_dict


def article_spider(request):
    url_dict = {}
    for i in range(30):
        url = 'https://cloud.tencent.com/developer/column/5263/page-' + str(i)
        print(f'爬取第{i + 1}页')
        url_sigle_dict = get_article_page(url)
        url_dict = dict(url_dict, **url_sigle_dict)
    return HttpResponse(url_dict)
