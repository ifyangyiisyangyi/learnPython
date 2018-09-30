# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'https://book.douban.com/top250'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
r = requests.get(url,headers)
print(r.status_code)
# print(r.headers)
html = r.content

soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify())
print(soup.get_text())


