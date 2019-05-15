
import requests
import json
from api import get_robot_token
from conf import read_yaml


globle_udid = "FRFFBZYP"
token = get_robot_token.get_robot_token(globle_udid)


def robot_login(udid):
    urll = read_yaml.test_data["url"] + "/robot-login"
    headers = {
        "Accept": "application/vnd.luka." + read_yaml.test_data["api_version"] + "+json",
        "Content-Type": "application/json",
        "Accept-Language": read_yaml.test_data["lang"]
    }
    data = {
        "data": {
            "type": "robot-login",
            "attributes": {
                "udid": udid
            }
        }
    }
    result = requests.put(url=urll, headers=headers, data=json.dumps(data))
    result = json.loads(result.text)
    return result



def cv_model_book(book_id):
    url = read_yaml.test_data["url"] + "/cv/model/book/" + book_id
    headers = {
        "Authorization": "Bearer" + token,
        "Accept": "application/vnd.luka.v1.14+json"
    }
    data = {

    }
    result = requests.get(url=url, headers=headers, data=json.dumps(data))
    result = json.loads(result.text)
    result = result["errmsg"]
    return result


if __name__ == '__main__':
    print(token)
