'''
爬取boss直聘岗位信息
'''
import requests
import re
from bs4 import BeautifulSoup
import json

def get_html(url):

    headers = {
        'referer' : 'https://www.zhipin.com/job_detail/?query=&city=101010100&industry=&position=',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    # params = {
    #     'query' : '自动化测试',
    #     'city' : '101010100'
    # }
    try:
        r = requests.request('get', url = url,  headers = headers)
    except:
        print("请求出错啦")
        return 
    else:
        html = r.content
        
        return html

def get_con(html):
    soup = BeautifulSoup(html, 'html.parser')
    job_list = soup.find('div', attrs = {'class' : 'job-list'}) # 找到岗位信息
    page = soup.find('div', attrs = {'class' : 'page'}) # 找到页码信息
    next_page = page.find('a', attrs = {'class' : 'next'}).get('href')
  
    for i in job_list.find_all('li'): 
        job_info = {}
        companyName = i.find('div', attrs = {'class' : 'info-company'}).find('div', attrs = {'class' : 'company-text'}).find('h3', attrs = {'class' : 'name'}).find('a').string
        position = i.find('div', attrs = {'class' : 'info-primary'}).find('h3', attrs = {'class' : 'name'}).find('div', attrs = {'class' : 'job-title'}).string
        salary = i.find('div', attrs = {'class' : 'info-primary'}).find('h3', attrs = {'class' : 'name'}).find('span', attrs = {'class' : 'red'}).string
        other = i.find('div', attrs = {'class' : 'info-primary'}).find('p')
        other = [text.strip() for text in other.find_all(text=True) if text.parent.name !='em' and text.strip()]
        job_info['companyName'] = companyName
        job_info['position'] = position
        job_info['salary'] = salary
        job_info['other'] = other
        job_info = json.dumps(job_info, ensure_ascii=False)
        print('****************************')
        print(job_info, type(job_info))
        with open('job_info.txt', 'a+') as f:
            f.write(job_info + '\n')
            
                
    if next_page != 'javascript':
        return next_page
    else:
        return None


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
    while url:
        html = get_html(url)
        query = get_con(html)
        url = 'https://www.zhipin.com' + query
if __name__ == "__main__":
    main()