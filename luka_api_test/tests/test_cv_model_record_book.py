import pytest

from conf import read_env
from api.interface import cv_model_record_book


class TestCase:
    @pytest.mark.smoke
    @pytest.mark.skipif(read_env.test_data['api_version'] != 'luka.v1.15', reason="接口版本低于v1.15")
    def test_cv_model_record_book(self):
        print('获取拍录绘本信息')
        assert cv_model_record_book('52515F07-6758-4348-A424-A1DC6B3A5D82')['errmsg'] == 'success'
