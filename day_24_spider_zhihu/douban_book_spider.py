import requests
from bs4 import BeautifulSoup

url = 'https://book.douban.com/top250'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
html = requests.get(url, headers = header).content
soup = BeautifulSoup(html, 'html.parser')
book_list = soup.find('div', attrs = {'class': 'indent'})    # 书单
page = soup.find('div', attrs = {'class': 'paginator'}) 
next_page = soup.find('span', attrs = {'class': 'next'}).find('a') 
print(next_page)
