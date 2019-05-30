import time
import pytest
import os


def save_reports(device_type):
    report_path = os.path.join(os.path.abspath('.'), 'report/')
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

    if device_type == 'luka':
        luka_report_name = report_path + 'luka-' + now + '.html'
        pytest.main(['-v', '--html=' + luka_report_name, '--self-contained-html'])
    elif device_type == 'baby':
        baby_report_name = report_path + 'baby-' + now + '.html'
        pytest.main(['-m', 'baby', '-v', '--html=' + baby_report_name, '--self-contained-html'])
    else:
        print('无效的设备类型')


if __name__ == '__main__':
    print(int(time.time()))
