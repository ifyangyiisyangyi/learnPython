# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

DOWNLOAD_URL = 'http://movie.douban.com/top250/'

# 获取网页内容
def download_page(url):
	headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'}
	data = requests.get(url, headers = headers).content
	return data

# 分解页面信息
def get_li(doc):
	soup = BeautifulSoup(doc, 'html.parser') # 创建一个html文本解析的对象
	ol = soup.find('ol', class_ = 'grid_view')  # 获取html页面的有序列表内容
	name = [] # 片名
	star_con = [] # 评价人数
	score = [] #评分
	info_list = [] #短评
	for i in ol.find_all('li'):
		detail = i.find('div' , attrs = {'class' : 'hd'}) # 获取列表项目
		movie_name = detail.find('span', attrs = {'class' : 'title'}).get_text() # 获取片名
		# print(movie_name)
		detail2 = i.find('div', attrs = {'class', 'bd'})
		star = i.find('div', attrs = {'class' : 'star'})
		# print(star)
		star_num = star.find(text = re.compile('评价'))  # 评价人数
		print(star_num)
		score_single = detail2.find('span', attrs = {'class' : 'rating_num'}).get_text() # 评分
		# print(score_single)
		comment = detail2.find('span', attrs = {'class' : 'inq'}).get_text() # 短评
		# print(comment)

doc = download_page(DOWNLOAD_URL)
get_li(doc)


