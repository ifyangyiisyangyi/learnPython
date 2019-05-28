import os
import json

from utils.save_reports import save_reports


def main(device_type='luka', **kwargs):
    current_env_dict = {}
    for key in kwargs:
        current_env_dict[key] = kwargs[key]

    env_path = os.path.join(os.path.abspath('.'), 'conf/current_env.json')
    with open(env_path, 'w') as f:
        json.dump(current_env_dict, f)  # 保存环境变量

    save_reports(device_type)

    if (os.path.exists(env_path)):  # 删除保存环境变量的临时json文件
        os.remove(env_path)
    else:
        print('current_env is not exists~')


if __name__ == '__main__':
    '''
    默认环境变量
    device_type = 'luka'
    url = 'http://luka-api.test1.k8s-qa.linglove.cn
    api_version = 'luka.v1.15'
    lang = 'zh_CN'
    udid = '24NQRQJZ27'
    '''
    main()
