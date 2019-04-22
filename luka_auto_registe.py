

import requests
import json
import pymysql
import re
from time import sleep

url = "http://luka-api.test1.k8s-qa.linglove.cn"  # 测试环境地址
name = "18101287746"                             # 要注册的手机号码

def send_captcha(url):
    print("发送验证码...")
    urll = url + "/send-captcha"
    headers = {
        "Accept": "application/vnd.luka.v1.15+json",
        "Content-Type": "application/json",
        "Accept-Language": "zh_CN"
    }
    data = {
        "data": {
            "type": "send-captcha",
            "attributes": {
                "region": "CN",
                "name": name,
                "captcha_type": 1
            }
        }
    }
    result = requests.post(url=urll, headers=headers, data=json.dumps(data))
    print(result.status_code)
    print(result.text)
    return

def get_captcha():
    print("查数据库...")
    db = pymysql.connect("localhost", "root", "123", "account")
    cursor = db.cursor()
    # cursor.execute("select version()")
    # data = cursor.fetchone()
    # print ("Database version : %s " % data)
    sql_str = "手机号" + name + "的验证码%"
    sql = "select description from activity_log where description like" + "'" + sql_str + "'"
    print(sql)
    # sql = "select description from activity_log where description like '手机号18101287746的验证码%'"
    cursor.execute(sql)
    captcha_result = cursor.fetchone()
    # print(type(captcha_result))
    if type(captcha_result) == tuple:
        captcha_result = captcha_result[0]
        captcha = re.findall("\d\d\d\d", captcha_result)[2]
        print("验证码是：" + captcha)
        return captcha
    else:
        print("没有查到验证码！！！")
        return

def app_register():
    captcha = get_captcha()
    print("注册开始执行")
    urll = url + "/app-register"
    headers = {
        "Accept": "application/vnd.luka.v1.15+json",
        "Content-Type": "application/json",
        "Accept-Language": "zh_CN"
    }
    data = {
        "data": {
            "type": "app-register",
            "attributes": {
                    "region": "CN",
                    "name": name,
                    "password": "123456a",
                    "captcha": captcha
            }
        }
    }
    result = requests.post(url=urll, headers=headers, data=json.dumps(data))
    print(result.status_code)
    print(result.text)
    return

if __name__ == "__main__":
    send_captcha(url)
    print("等待20s...")
    sleep(20)
    app_register()
