'''
learn beautiful
'''
from bs4 import BeautifulSoup
import lxml

html = """
<html><head><title>标题</title></head>
<body>
<p class="title" name="dromouse"><b>标题2</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml') # 创建BeautifulSoup对象
# print(soup.prettify())
print(soup.title) # 获取Tags
print(soup.head)
# print(soup.a,type(soup.a))
# print(soup.a.name)
print(soup.title.string, type(soup.title.string)) # 得到标签的内容，可以用.string获取标签内部的文字
print(soup.p.string)
print(soup.select('title'))