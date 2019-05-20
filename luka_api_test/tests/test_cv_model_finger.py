import pytest

from api.interface import cv_model_finger


class TestCase:
    @pytest.mark.smoke
    def test_cv_model_finger_case1(self):
        print('获取手指模型')
        assert cv_model_finger()['errmsg'] == 'success'
