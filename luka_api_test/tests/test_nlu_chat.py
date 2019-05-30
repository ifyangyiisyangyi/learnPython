import os

import pytest

from api.interface import nlu_chat
from tests.conftest import nlu_words

with open(os.getcwd() + r'\testdata\nludata.txt', 'r+', encoding='utf-8') as f:
    words = f.readlines()


class TestCase:
    @pytest.mark.smoke
    @pytest.mark.baby
    def test_nlu_chat_case1(self):
        print('nlu-我想听恐龙大陆')
        assert nlu_chat('我想听恐龙大陆')['errmsg'] == 'success'

    @pytest.mark.baby
    def test_nlu_chat_case2(self):
        print('nlu-我想听蓝精灵')
        assert nlu_chat('我想听蓝精灵')['errmsg'] == 'success'

    @pytest.mark.baby
    def test_nlu_chat_case3(self):
        print('nlu-一加一等于几')
        assert nlu_chat('一加一等于几')['errmsg'] == 'success'
        print(nlu_chat('一加一等于几'))

    @pytest.mark.baby
    def test_nlu_chat_case4(self):
        for i in words:
            print(i)
            assert nlu_chat(i)['errmsg'] == 'success'

    @pytest.fixture(params=words)  # case5:测试数据参数化
    def test_data(self):
        return words

    def test_nlu_chat_case5(test_data):
        assert nlu_chat(words)['errmsg'] == 'success'

    def test_nlu_chat_case6(self):  # 数据保存在conftest.py文件中
        print(nlu_words)
        assert nlu_chat(nlu_words)['errmsg'] == 'success'
