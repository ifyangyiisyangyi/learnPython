import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse, JsonResponse

from TestModel.models import spider_article


def get_article_page(url):
    r = requests.request('get', url=url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    ls = soup('h3', class_="com-blog-panel-title")
    url_dict = {}
    for tag in ls:
        s = 'https://cloud.tencent.com' + tag.a['href']
        title = tag.a.string
        article = spider_article(title=title,
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
    return JsonResponse(url_dict)