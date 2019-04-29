import pytest
import requests
import json
import read_yaml

# 获取token
def get_robot_token(udid):
    urll = read_yaml.test_data["url"] + "/robot-login"
    headers = {
        "Accept": "application/vnd.luka." + read_yaml.test_data["api_version"] + "+json",
        "Content-Type": "application/json",
        "Accept-Language": read_yaml.test_data["lang"]
    }
    data = {
        "data": {
            "type": "robot-login",
            "attributes": {
            "udid": udid
            }
        }
    }
    result = requests.put(url = urll, headers = headers, data = json.dumps(data))
    # result = json.loads(result.text)
    token = result.json()["data"]["token"]
    return token

