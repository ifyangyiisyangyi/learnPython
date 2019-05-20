import pytest
from api.interface import cv_model_cover


class TestCase:
    @pytest.mark.smoke
    def test_cv_model_cover_case1(self):
        print("获取封面模型")
        assert cv_model_cover()['errmsg'] == "success"
