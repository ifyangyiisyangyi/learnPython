import pytest
import json
from api.interface import cv_model_book


class TestCase:
    @pytest.mark.smoke
    def test_book_read_case1(self):
        print("绘本id 50测试")
        assert cv_model_book("50") == "success"

    @pytest.mark.skip(reason = "skip跳过")     # 标记为跳过，不执行该用例
    def test_book_read_case2(self):
        assert cv_model_book("415") == "success"

    @pytest.mark.skipif(json.__version__ > "100", reason = "skipif跳过这条用例")
    def test_book_read_case3(self):
        assert cv_model_book("12047") == "success"