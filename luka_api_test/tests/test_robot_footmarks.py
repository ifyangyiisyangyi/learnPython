import time

from api.interface import robot_footmarks


class TestCase:
    def test_robot_footmarks_case1(self):
        print('播放足迹请求成功')
        assert robot_footmarks('a488f2542ceeaed6560a5ee50ede232a', int(time.time()))['errmsg'] == 'success'
        print('播放足迹添加成功')
        assert robot_footmarks('a488f2542ceeaed6560a5ee50ede232a', int(time.time()))['data']['failed_ids'] == []