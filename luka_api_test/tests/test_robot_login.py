import pytest
from api.interface import robot_login


class TestCase:
    @pytest.mark.smoke
    def test_robot_login_case1(self):
        print("8位设备码测试")
        assert robot_login("FRFFBZYP")['errmsg'] == "success"
