import pytest

from api.interface import nlu_chat
from utils.analysis_base64 import analysis_base64


class TestCase:
    @pytest.mark.smoke
    def test_nlu_chat_case1(self):
        print('nlu-我想听恐龙大陆')
        assert nlu_chat('我想听恐龙大陆')['errmsg'] == 'success'
    def test_nlu_chat_case2(self):
        print('nlu-我想听蓝精灵')
        result = nlu_chat('蓝精灵')
        assert "蓝精灵" in analysis_base64(result)
    def test_nlu_chat_case3(self):
        print('nlu-一加一等于几')
        assert nlu_chat('一加一等于几')['errmsg'] == 'success'