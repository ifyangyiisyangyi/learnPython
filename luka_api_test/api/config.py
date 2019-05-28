"""
保存token
"""

from utils.get_robot_token import get_robot_token
from conf import read_env

udid = read_env.test_data['udid']
result = get_robot_token(udid)
token = result

if __name__ == '__main__':
    print(token)
