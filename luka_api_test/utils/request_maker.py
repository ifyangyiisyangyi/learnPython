import json

import requests

from conf import read_env
from api.config import token


def get_request_maker(request_type, url_suffix, data=None):
    """
    :param request_type: 请求类型
    :param url_suffix:  url后缀
    :param data: data
    :return: json
    """
    if data is None:
        data = {}
    if request_type == 'get':
        url = "{}".format(read_env.test_data["url"]) + url_suffix
        headers = {
            "Authorization": "Bearer" + token,
            "Accept": "application/vnd.luka.{}+json".format(read_env.test_data["api_version"])
        }
        result = requests.get(url=url, headers=headers, data=json.dumps(data))
        return result.json()
    elif request_type == 'put':
        url = "{}".format(read_env.test_data["url"]) + url_suffix
        headers = {
            "Accept": "application/vnd.luka.{}+json".format(read_env.test_data["api_version"]),
            "Content-Type": "application/json",
            "Accept-Language": read_env.test_data["lang"]
        }
        result = requests.put(url=url, headers=headers, data=json.dumps(data))
        return result.json()
    elif request_type == 'post':
        url = "{}".format(read_env.test_data["url"]) + url_suffix
        headers = {
            "Authorization": "Bearer" + token,
            "Accept": "application/vnd.luka.{}+json".format(read_env.test_data["api_version"]),
            "Content-Type": "application/json",
            "Accept-Language": read_env.test_data["lang"]
        }
        result = requests.post(url=url, headers=headers, data=json.dumps(data))
        return result.json()
    else:
        return


if __name__ == '__main__':
    pass
