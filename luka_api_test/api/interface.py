"""
接口文件
"""

import requests
import json

from api.config import token
from conf import read_env


def robot_login(udid):
    url = read_env.test_data["url"] + "/robot-login"
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
    result = requests.put(url=url, headers=headers, data=json.dumps(data))
    result = json.loads(result.text)
    return result


def cv_model_book(book_id):
    url = read_env.test_data["url"] + "/cv/model/book/" + book_id
    headers = {
        "Authorization": "Bearer" + token,
        "Accept": "application/vnd.luka.v1.14+json"
    }
    data = {

    }
    result = requests.get(url=url, headers=headers, data=json.dumps(data))
    result = json.loads(result.text)
    result = result["errmsg"]
    return result


def robots_me():
    url = read_env.test_data["url"] + "/robots-me"
    headers = {
        "Authorization": "Bearer" + token,
        "Accept": "application/vnd.luka.v1.14+json"
    }
    data = {

    }
    result = requests.get(url=url, headers=headers, data=json.dumps(data))
    result = json.loads(result.text)
    return result


if __name__ == '__main__':
    pass
