import pytest

from api.interface import robots_me


class TestCase:
    @pytest.mark.smoke
    @pytest.mark.baby
    def test_robots_me_case1(self):
        print("成功获取robot关联的用户信息")
        assert robots_me()['errmsg'] == "success"

    def test_robots_me_case2(self):
        print('判断设备类型')
        assert robots_me()['data']['robot']['device_type'] == 'lukapro'
        print('判断时区')
        assert robots_me()['data']['robot']['timezone'] == 'Asia/Shanghai'

    def test_robots_me_case3(self):
        print('绑定状态')
        assert robots_me()['data']['users'] != None
