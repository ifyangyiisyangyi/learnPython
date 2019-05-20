import pytest

from api.interface import record_books_cover_model


class TestCase:
    @pytest.mark.smoke
    def test_record_books_cover_model_case1(self):
        print("获取拍录绘本封面")
        assert record_books_cover_model()['errmsg'] == 'success'