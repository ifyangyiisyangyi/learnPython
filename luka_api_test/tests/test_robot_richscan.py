from api.interface import robot_richscan
import pytest

class TestCase:
    @pytest.mark.smoke
    def test_robot_richscan_case1(self):
        print("设备扫一扫")
        assert robot_richscan('50')['errmsg'] == "success"