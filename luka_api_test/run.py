import pytest
import os
import time
import json


def main(device_type='luka', **kwargs):
    current_env_dict = {}
    for key in kwargs:
        current_env_dict[key] = kwargs[key]

    env_path = os.path.join(os.path.abspath('.'), 'conf/current_env.json')
    with open(env_path, 'w') as f:
        json.dump(current_env_dict, f)

    print(os.path.abspath('.'))
    report_path = os.path.join(os.path.abspath('.'), 'report/')
    print(report_path)
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

    if device_type == 'luka':
        luka_report_name = report_path + 'luka-' + now + '.html'
        pytest.main(['-v', '--html=' + luka_report_name, '--self-contained-html'])
    elif device_type == 'baby':
        baby_report_name = report_path + 'baby-' + now + '.html'
        pytest.main(['-m', 'baby', '-v', '--html=' + baby_report_name, '--self-contained-html'])

    if (os.path.exists(env_path)):
        os.remove(env_path)
    else:
        print('current_env is not exists~')

if __name__ == '__main__':
    main()
