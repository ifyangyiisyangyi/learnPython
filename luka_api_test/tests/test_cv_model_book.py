import pytest
import json
from conf import read_env
from api.interface import cv_model_book


class TestCase:
    @pytest.mark.smoke
    def test_book_read_case1(self):
        print("绘本id 50测试")
        if read_env.test_data['api_version'] == 'luka.v1.15':
            assert cv_model_book("b15d8cf9-720f-c21f-ec86-33fb952c3ce9")['errmsg'] == "success"
        else:
            assert cv_model_book("50")['errmsg'] == "success"

    @pytest.mark.skip(reason="skip跳过")  # 标记为跳过，不执行该用例
    def test_book_read_case2(self):
        assert cv_model_book("415")['errmsg'] == "success"

    @pytest.mark.skipif(json.__version__ > "100", reason="skipif跳过这条用例")
    def test_book_read_case3(self):
        assert cv_model_book("12047")['errmsg'] == "success"
