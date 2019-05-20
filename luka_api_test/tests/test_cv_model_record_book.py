import pytest

from api.interface import cv_model_record_book


class TestCase:
    @pytest.mark.smoke
    def test_cv_model_record_book(self):
        print('获取拍录绘本信息')
        assert cv_model_record_book('52515F07-6758-4348-A424-A1DC6B3A5D82')['errmsg'] == 'success'