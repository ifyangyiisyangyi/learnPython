import pytest

from api.interface import cv_card_model


class TestCase:
    @pytest.mark.smoke
    def test_cv_card_model(self):
        print('获取卡片模型')
        assert cv_card_model()['errmsg'] == 'success'
