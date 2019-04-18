import requests
import json

name = "18859285396"
password = "123456a"
udid = "FRFFBZYP"

url = "http://luka-api.test1.k8s-qa.linglove.cn"

# 获取app登录token

def get_app_token(url):
    urll = url + "/app-login"
    headers = {
        "Accept": "application/vnd.luka.v1.15+json",
        "Content-Type": "application/json",
        "Accept-Language": "zh_CN"
    }
    data = {
        "data": {
            "type": "app-login",
            "attributes": {
                "region": "CN",
                "name": name,
                "password": password
            }
        }
    }
    result = requests.put(urll, headers=headers, data=json.dumps(data))
    result = json.loads(result.text)
    token = result["data"]["token"]
    return token

# 获取user_id

def get_user_id(token):
    urll = url + "/users-me"
    Authorization = "Bearer" + token
    headers = {
        "Authorization":Authorization,
        "Accept": "application/vnd.luka.v1.15+json",
        "Content-Type": "application/json",
        "Accept-Language": "zh_CN"
    }
    result = requests.get(urll, headers = headers)
    result = json.loads(result.text)
    user_id = result["data"]["user"]["id"]
    return user_id

print(get_user_id(get_app_token(url)))


# 获取设备登录token

def get_robot_token(url):
    url = url + "/robot-login"
    headers = {
        "Accept": "application/vnd.luka.v1.15+json",
        "Content-Type": "application/json",
        "Accept-Language": "zh_CN"
    }
    data = {
        "data": {
            "type": "robot-login",
            "attributes": {
            "udid": udid
            }
        }
    }
    result = requests.put(url = url, headers = headers, data = json.dumps(data))
    result = json.loads(result.text)
    token = result["data"]["token"]
    return token

# robot登录
def robot_login(url):
    url = url + "/robot-login"
    headers = {
        "Accept": "application/vnd.luka.v1.15+json",
        "Content-Type": "application/json",
        "Accept-Language": "zh_CN"
    }
    data = {
        "data": {
            "type": "robot-login",
            "attributes": {
            "udid": udid
            }
        }
    }
    result = requests.put(url = url, headers = headers, data = json.dumps(data))
    print("yy")
    return

robot_login(url)