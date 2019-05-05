

import pytest
import requests
import json


url = "http://luka-api.test1.k8s-qa.linglove.cn"

def robot_login(udid):
    urll = url + "/robot-login"
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
    result = requests.put(url = urll, headers = headers, data = json.dumps(data))
    result = json.loads(result.text)
    result = result["errmsg"]
    return result

def get_robot_token(udid):
    urll = url + "/robot-login"
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
    result = requests.put(url = urll, headers = headers, data = json.dumps(data))
    result = json.loads(result.text)
    token = result["data"]["token"]
    return token


class TestCase():
    @pytest.mark.smoke   # 标记为冒烟测试用例
    def test_robot_login_case1(self):
        print("luka 8 位设备码测试")
        assert robot_login("FRFFBZYP") == "success"
    @pytest.mark.p1    # 标记为P1测试用例
    def test_robot_login_case2(self):
        print("luka hero 10 位设备码测试")
        assert robot_login("24NQRQ9Z2L") == "success"


