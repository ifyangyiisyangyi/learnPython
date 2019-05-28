import pytest

from api.interface import robots_me


class TestCase:
    @pytest.mark.smoke
    @pytest.mark.baby
    def test_robots_me_case1(self):
        print("获取robot关联的用户信息")
        assert robots_me()['errmsg'] == "success"
