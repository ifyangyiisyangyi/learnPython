"""
接口文件
"""

from utils.request_maker import request_maker


def robot_login(udid):  # robot登录
    data = {
        "data": {
            "type": "robot-login",
            "attributes": {
                "udid": udid
            }
        }
    }
    return request_maker('put', '/robot-login', data)


def cv_model_cover():  # 获取封面模型
    return request_maker('get', '/cv/model/cover')


def record_books_cover_model():  # 获取拍录绘本封面模型
    return request_maker('get', '/record-books/cover/model')


def cv_model_finger():  # 获取手指模型
    return request_maker('get', '/cv/model/finger')


def cv_model_book(book_id):  # 获取绘本模型
    url = "/cv/model/book/" + book_id
    return request_maker('get', url)


def cv_card_model():  # 获取卡片模型
    return request_maker('get', '/cv/card-models/0/latest')


def cv_cards():  # 获取卡片信息
    return request_maker('get', '/cv/cards/{card}')


def cv_model_record_book(record_book_id):  # 获取拍录绘本详情
    url = '/cv/model/record_book/' + record_book_id
    return request_maker('get', url)


def bookshelf_voice():  # 获取书架音频
    return request_maker('get', '/robots-me/relationships/bookshelf/voices?page[number]=1&page[size]=10')


def robots_me():  # 获取设备信息
    return request_maker('get', '/robots-me')


def robot_richscan(book_id):  # 设备扫一扫
    data = {
        "data": {
            "type": "bookshelf",
            "attributes": {
                "alg_book_id": book_id
            }
        }
    }
    return request_maker('post', '/robot-richscan', data)


def del_favorites():  # 单曲删除收藏
    data = {
        "data": [
            {
                "type": "favorites",
                "attributes": {
                    "track_id": "57e506702d48039e043d2d2e"
                }
            },
            {
                "type": "favorites",
                "attributes": {
                    "track_id": "57e5063f2d48039e043d2ac0"
                }
            }
        ]
    }
    return request_maker('delete', '/favorites', data)


def nlu_chat(words):  # nlu闲聊
    data = {
        "data": {
            "type": "nlu",
            "attributes": {
                "words": words,
                "nlu_version": "3.2",
                "device_status": "idle",
                "user_id": "luka_001",
                "machine_sentence": "",
                "initiative": False,
                "event_id": 0,
                "resource_version": 0,
                "child_id": 0
            }
        }
    }
    return request_maker('post', '/nlu/chat', data)


def robot_footmarks(track_id, time):  # 播放足迹
    data = {
        "footmarks": [
            {
                "id": track_id,
                "timestamp": time
            }
        ],
        "type": 0
    }
    return request_maker('post', '/robot-footmarks', data)


def robot_books(picture_book_ids):  # 获取绘本模式及音频
    data = {
        "data": {
            "type": "picture-book",
            "attributes": {
                "picture_book_ids": picture_book_ids
            }
        }
    }
    return request_maker('post', '/robot/books', data)


if __name__ == '__main__':
    print(robot_footmarks("a488f2542ceeaed6560a5ee50ede232a", 1559197680))
