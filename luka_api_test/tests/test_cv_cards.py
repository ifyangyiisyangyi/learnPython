import pytest

from api.interface import cv_cards


class TestCase:
    @pytest.mark.smoke
    def test_cv_cards(self):
        print('获取卡片信息')
        assert cv_cards()['errmsg'] == 'success'
