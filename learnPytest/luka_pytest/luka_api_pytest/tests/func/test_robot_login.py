import pytest
import robot_login

class Test():
    def test_udid(self, udid_8_success):
        assert robot_login.robot_login(udid_8_success) == "success"
