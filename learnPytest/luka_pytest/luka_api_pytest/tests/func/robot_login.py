'''
luka设备登录接口
'''

import pytest
import requests
import json

def robot_login(udid):
    url = offline_url + "/robot-login"
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
    return result