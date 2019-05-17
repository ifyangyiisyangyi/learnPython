from api.interface import robot_richscan
import pytest

class TestCase:
    @pytest.mark.smoke
    def test_robot_richscan_case1(self):
        print("设备扫一扫")
        assert robot_richscan('8ef0d0d0-4829-e49a-e7cd-83ceffdccc6c')['errmsg'] == "success"