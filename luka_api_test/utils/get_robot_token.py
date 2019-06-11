"""
获取token

"""

import requests
import json

from conf import read_env

"""
get_robot_token方法加装饰器，统计方法调用次数
"""
class CallingCounter(object):
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@CallingCounter
def get_robot_token(udid):
    urll = read_env.test_data["url"] + "/robot-login"
    headers = {
        "Accept": f'application/vnd.{read_env.test_data["api_version"]}+json',
        "Content-Type": "application/json",
        "Accept-Language": read_env.test_data["lang"]
    }
    data = {
        "data": {
            "type": "robot-login",
            "attributes": {
                "udid": udid
            }
        }
    }
    result = requests.put(url=urll, headers=headers, data=json.dumps(data))
    token = result.json()["data"]["token"]
    return token
