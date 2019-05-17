"""
获取token

"""

import requests
import json

from conf import read_env


def get_robot_token(udid):
    urll = read_env.test_data["url"] + "/robot-login"
    headers = {
        "Accept": "application/vnd.luka." + read_env.test_data["api_version"] + "+json",
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
