"""
爬取未闻code的文章和标题
"""

import requests
from bs4 import BeautifulSoup


def get_article_page(url):
    r = requests.request('get', url=url)
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    ls = soup('h3', class_="com-article-panel-title")
    url_dict = {}
    for tag in ls:
        s = 'https://cloud.tencent.com' + tag.a['href']
        title = tag.a.string
        url_dict[title] = s  # 返回文章的标题和链接
    return url_dict


def get_article_all():
    url_dict = {}
    for i in range(30):
        url = 'https://cloud.tencent.com/developer/column/5263/page-' + str(i)
        print(f'爬取第{i + 1}页')
        url_sigle_dict = get_article_page(url)
        url_dict = dict(url_dict, **url_sigle_dict)
    return url_dict


if __name__ == '__main__':
    s = get_article_all()
    print(s)
    print(len(s))
