import requests
import json
import re
from time import sleep
import random

url = "https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput="

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Referer":"https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E8%87%AA%E5%8A%A8%E5%8C%96?oquery=%E6%B5%8B%E8%AF%95&fromSearch=true&labelWords=relative&city=%E5%8C%97%E4%BA%AC",
    "Host":"www.lagou.com",
    "Content-type":"application/json;charset=utf-8"
}
'''
def get_page_info():
    r = requests.get(url = url, headers = headers)
    return r.text

print(get_page_info())
'''

# sum = 0
for i in range(0, 10):

    r = requests.get(url = url, headers = headers)
    print(r.status_code)
    print(r.encoding)
    result = r.text
    print(type(result))
    r.encoding = r.apparent_encoding
    html = r.text  
    print(html)

    data = re.findall('.*Words=relative">(.*)</a></li>.*', html)
    print(data)
    if(data == []):
        sum += 1
    for i in data:
        print(i)   # 打印出招聘职位名称
    sleep(random.randint(3, 10))  # 设置随机3-10s请求一次，发现有时候请求不到结果
    sleep(10) # 设置10s请求一次，看看结果如何？
print("失败次数：" + str(sum))


