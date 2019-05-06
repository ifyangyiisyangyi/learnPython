'''
爬取boss直聘岗位信息
'''
import requests
import re
from bs4 import BeautifulSoup

def get_html(url):

    # url = 'https://www.zhipin.com/job_detail/?query=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&city=101010100&industry=&position='
    headers = {
        'referer' : 'https://www.zhipin.com/job_detail/?query=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&city=101010100&industry=&position=',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    # params = {
    #     'query' : '自动化测试',
    #     'city' : '101010100'
    # }
    r = requests.request('get', url = url,  headers = headers)
    # print(r.status_code)
    html = r.content
    # print(html)
    return html

def get_con(html):
    soup = BeautifulSoup(html, 'html.parser')
    positon_list = soup.find('div', attrs = {'class' : 'job-list'}) # 找到岗位信息
    page = soup.find('div', attrs = {'class' : 'page'}) # 找到页码信息
    next_page = page.find('a', attrs = {'class' : 'next'})
    # print(next_page.get('href'))
    name = []
    for i in positon_list.find_all('li'): 
        position = i.find('div', attrs = {'class' : 'info-company'})
        position = position.find('div', attrs = {'class' : 'company-text'})
        position = position.find('h3', attrs = {'class' : 'name'})
        position = list(position.find('a').string)        # 把岗位名称提取出来
        if len(position) > 1:
            x = position[0] + position[1]
        else:
            x = position[0]
        name.append(x)
    if next_page:
        return name, next_page.get('href')
    else:
        return name, None


class PositionInfo(object):
    def __init__(self, compamyName, position, salary, city):
        self.compamyName = compamyName
        self.position = position
        self.salary = salary
        self.city = city

    def showInfo(self):
        print(self.compamyName)
        print(self.position)
        print(self.salary)
        print(self.city)
        print('************************************************')

def main():
    url = 'https://www.zhipin.com/job_detail/?query=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&city=101010100&industry=&position='
    # query = '/job_detail/?query=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&city=101010100&industry=&position='
    # url = url + query
    
    position_list = []
    while url:
        # query = '/job_detail/?query=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&city=101010100&industry=&position='
        # url = url + query
        html = get_html(url)
        name, query = get_con(html)
       
        url = 'https://www.zhipin.com' + query
        position_list = position_list + name
   
        for i in position_list:
            print(i)
if __name__ == "__main__":
    main()