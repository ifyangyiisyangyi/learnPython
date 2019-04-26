

import test_robot_login
import pytest
import requests
import json

url = "http://luka-api.test1.k8s-qa.linglove.cn"
udid = "FRFFBZYP"
book_id = "50"

def cv_model_book(book_id):
    token = test_robot_login.get_robot_token(udid)
    # print(token)
    urll = url + "/cv/model/book/" + book_id
    # print(urll)
    headers = {
        "Authorization":"Bearer" + token,
        "Accept":"application/vnd.luka.v1.14+json"
    }
    data = {

    }
    result = requests.get(url = urll,headers = headers, data = json.dumps(data))
    result = json.loads(result.text)
    result = result["errmsg"]
    return result

class TestCase():
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