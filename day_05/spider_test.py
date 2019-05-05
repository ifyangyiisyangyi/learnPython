import requests
import re

# 获取到网页信息
def getPageInfo():
    # url = 'https://www.zhipin.com/job_detail/?query=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&city=101010100&industry=&position='
    url = 'https://www.zhipin.com/c101010100/?query=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&page=2&ka=page-next'
    headers = {
        # 'referer' : 'https://www.zhipin.com/',
        'referer' : 'https://www.zhipin.com/job_detail/?query=%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95&city=101010100&industry=&position=',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
    r = requests.get(url = url, headers = headers)
    r.encoding = 'utf-8'
    html = r.text
    return html

html = getPageInfo()

jobTitle = re.findall('.*<div class="job-title">(.*)</div>', html)
salary = re.findall('.*\<span class="red">(.*).*</span>', html)
companyFullName = re.findall('.*target="_blank">(.*)</a></h3>', html)


for i in range(30):
    print( companyFullName[i], salary[i], jobTitle[i])