import requests
from bs4 import BeautifulSoup
import re

url = 'https://cloud.tencent.com/developer/column/5263/page-0'

headers = {
    'user_Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'cookie' : '_ga=GA1.2.498134757.1553608057; qcloud_uid=6eef2b3a1d4d1da42fd1d92cecdb92db%40devS; pgv_pvi=148392960; language=zh; _gcl_au=1.1.1471091045.1570516856; intl=; qcmainCSRFToken=B1g8bQUgiS; qcloud_visitId=56b04eeda033ee31934139cb5e76420d; qcloud_from=qcloud.baidu.seo-1573049091636; _gat=1; pgv_si=s7647547392'
}

r  = requests.request('get', url = url, headers = headers)
html = r.text
# print(html)
soup = BeautifulSoup(html, 'lxml')
# htmlList = soup.find('div', attrs={'class' : 'com-article-list'})   # 解析出class = com-article-list 属性的标签
# urlList = htmlList.find()
# print(soup.prettify())  # 格式化网页信息
# print(soup.title.name) # 获取标签名称
# print(soup.a['href']) # 获取匹配到的第一个标签的属性值
# print(soup.title.string) # 获取标签内容
print(soup.h3['class'])  # 获取第一个匹配的h3标签的class属性值
print(soup.h3.string) # 获取第一个匹配到的h3标签的内容
print(soup.h3.a['href'])   # 获取第一个匹配到的h3标签下嵌套的a标签的href属性值
htmlList = soup.find_all(attrs={'class' : 'com-article-panel-title'}) # 根据属性找出所有标签内容，返回列表
print(len(htmlList))
for i in htmlList:
    print(i)  # 打印h3标签内容
    print(type(i))
    print(re.findall('.*href="(.*)" style.*', str(i))[0]) # 打印一日一技的链接后缀

	
# test

