'''
登录接口测试
'''

import pytest
import requests
import json
import read_yaml

# robot 登录
def robot_login(udid):
    url =  "{0}/robot-login".format(read_yaml.test_data["url"])
    headers = {
        # "Accept": "application/vnd.luka." + read_yaml.test_data["api_version"] + "+json",
        "Accept": "application/vnd.luka.{0}+json".format(read_yaml.test_data["api_version"]),
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
    result = requests.put(url = url, headers = headers, data = json.dumps(data))
    result = json.loads(result.text)
    result = result["errmsg"]
    return result

class TestCase():
    @pytest.mark.smoke   # 标记为冒烟测试用例
    def test_robot_login_case1(self):
        print("luka 8 位设备码测试")
        assert robot_login("FRFFBZYP") == "success"
    @pytest.mark.p1    # 标记为P1测试用例
    def test_robot_login_case2(self):
        print("luka hero 10 位设备码测试")
        assert robot_login("24NQRQ9Z2L") == "success"
