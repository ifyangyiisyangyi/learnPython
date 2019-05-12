

from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests
from requests.packages import urllib3
from spider.viewmodels.job import Job
from spider.models.excel import save_as_xlsx
from spider.models.mysql import save_into_database
import json
import codecs


def prepare_request(args):
    str1 = '/job_detail/'
    str2 = '/wapi/zpgeek/mobile/jobs.json'
    path = str1 if args['front_page'] else str2
    headers = {
        'authority': 'www.zhipin.com',
        'method': 'GET',
        'path': path + '?' + urlencode(args['query_string']),
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'cookie': args['cookie'],
        'user-agent': 'Mozilla/5.0',
        'referer': args['referer']
    }
    if args['front_page']:
        headers['upgrade-insecure-requests'] = '1'
    else:
        headers['x-requested-with'] = 'XMLHttpRequest'
    params = args['query_string']
    return headers, params


def fetch(pages, cookie):
    data = []
    # front_html = fetch_front_page(cookie)
    # front_lis = create_dom(front_html, True)
    # print(len(front_lis))
    # data = get_data(front_lis, cookie)
    for page in range(1, pages):
        print('抓取第 ', page, '页')
        # print('执行')
        html = fetch_follow_pages(page, cookie)    # 把当前页的html抓到
        lis = create_dom(html, False)  # 把当前页面的30个岗位解析出来,返回soup对象的列表
        data += get_data(lis, cookie) # 解析页面，将岗位具体信息写成字典，保存在一个列表中
    jobs = create_job_model(data) # 构造job对象，保存在列表中
    # print('开始保存入数据库...')
    # save_into_database(jobs)
    # print('成功保存到数据库中')
    print('开始保存到Excel文件中')
    save_as_xlsx(jobs)
    print('成功保存到Excel文件中')


# def fetch_front_page(cookie):
#     query = {
#         'city': 101010100,
#         'source': 10,
#         'query': '技术'
#     }
#     front_page = True
#     referer = 'https://www.zhipin.com/?sid=sem_pz_bdpc_dasou_title'
#     args = {
#         'query_string': query,
#         'front_page': front_page,
#         'referer': referer,
#         'cookie': cookie
#     }
#
#     headers, params = prepare_request(args)
#     url = 'https://www.zhipin.com/job_detail/'
#     urllib3.disable_warnings()
#     content = ''
#     try:
#         res = requests.request('GET', url, headers=headers, params=params, verify=False)
#         res.raise_for_status()
#         res.encoding = res.apparent_encoding
#         content = res.text
#     except:
#         print('请求首页出现错误')
#     print(content)
#     return content


def fetch_follow_pages(page, cookie):
    if page < 1:
        print('page不能小于1')
        return
    query = {
        'city': 101010100,
        'page': page,
        'query': '测试开发'
    }
    front_page = False
    referer = 'https://www.zhipin.com/job_detail/?city=101010100&source=10&query=%E6%8A%80%E6%9C%AF'
    args = {
        'query_string': query,
        'front_page': front_page,
        'referer': referer,
        'cookie': cookie
    }
    headers, params = prepare_request(args)
    url = 'https://www.zhipin.com/wapi/zpgeek/mobile/jobs.json'
    urllib3.disable_warnings()
    content = ''
    try:
        res = requests.request('GET', url, headers=headers, params=params, verify=False)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        content = res.text
    except:
        print('请求第', page, '页失败')
    json_response = json.loads(content)
    return json_response['zpData']['html']


def create_dom(markup, front_page):
    soup = BeautifulSoup(markup, 'lxml')
    if front_page:
        div = soup.find_all('div', class_='job-list')[0]
        lis = div.find_all('li')
        print("找到所有job-list")
    else:
        lis = soup.find_all('li', class_='item')
    return lis   #返回ResultSet对象，也是一个列表？


def get_data(lis, cookie):
    infos = []
    keys = ['location', 'experience', 'education']
    for li in lis:
        info = {}
        url = li.find('a')['href']
        ka = li.find('a')['ka'] + '_blank'
        lid = li.find('a')['data-lid']
        detail_info = fetch_detail(url, {'ka':ka, 'lid':lid}, cookie)  # fetch_detail方法将岗位信息页面的hr和description解析出来
        info['hr'] = detail_info['hr']
        info['description'] = detail_info['description']
        company = li.find('div', class_='name').string
        info['company'] = company   # company信息从原网页中解析出来
        job = li.find('h4').string
        info['job'] = job
        salary = li.find('span', class_='salary').string
        info['salary'] = salary
        div = li.find('div', class_='msg')
        ems = div.find_all('em')
        for index, value in enumerate(ems):
            info[keys[index]] = value.string
        info['category'] = '技术'
        job_info = json.dumps(info, ensure_ascii= False)   # 把info转为字符串
        print(job_info)
        with codecs.open('job_info.txt', 'a+', encoding = 'utf-8') as f:
            f.write(job_info + '\n')
        infos.append(info)
    return infos  # 返回列表，里面有30个岗位的信息


def fetch_detail(url, query, cookie):
    query_string = 'ka='+query['ka'] + '&' + 'lid='+query['lid']
    url = 'https://www.zhipin.com' + url + '?' + query_string
    detail_info = {}
    args = {
        'query_string': query,
        'front_page': False,
        'referer': 'https://www.zhipin.com/job_detail/?city=101010100&source=10&query=%E6%8A%80%E6%9C%AF',
        'cookie': cookie
    }
    headers, _ = prepare_request(args)
    urllib3.disable_warnings()
    content = ''
    try:
        res = requests.request('GET', url, headers=headers, verify=False)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        content = res.text
    except:
        print('请求详情页数据出现错误')
    soup = BeautifulSoup(content, 'lxml')
    node = soup.find('h3', text='职位描述')
    hr = node.parent.parent.parent.find('h2', class_='name').text
    detail_info['hr'] = hr
    description = node.parent.find('div', class_='text').text
    detail_info['description'] = description.strip()
    return detail_info


def create_job_model(infos):
    print('data为:*****************', infos)
    data = []
    for info in infos:
        # print(info)
        data.append(Job(info))
    return data
