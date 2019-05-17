"""
接口文件
"""

from utils.request_maker import get_request_maker


def robot_login(udid): # robot登录
    data = {
        "data": {
            "type": "robot-login",
            "attributes": {
                "udid": udid
            }
        }
    }
    return get_request_maker('put', '/robot-login', data)


def cv_model_cover():
    return get_request_maker('get', '/cv/model/cover')


def cv_model_finger():
    return get_request_maker('get', '/cv/model/finger')


def cv_model_book(book_id):
    url = "/cv/model/book/" + book_id
    return get_request_maker('get', url)


def robots_me():
    return get_request_maker('get', '/robots-me')


def robot_richscan(book_id):
    data = {
        "data": {
            "type": "bookshelf",
            "attributes": {
                "alg_book_id": book_id
            }
        }
    }
    return get_request_maker('post', '/robot-richscan', data)


if __name__ == '__main__':
    print(robot_richscan())
