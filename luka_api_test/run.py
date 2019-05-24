import pytest
import os
import time


def main():
    print(os.path.abspath('.'))
    path = os.path.join(os.path.abspath('.'), 'report/')
    print(path)
    now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    luka_report_name = path + 'luka-' + now + '.html'
    # pytest.main(['-v', '--html=' + luka_report_name, '--self-contained-html'])

    baby_report_name = path + 'baby-' + now + '.html'
    pytest.main(['-m', 'baby', '-v', '--html=' + baby_report_name, '--self-contained-html'])


if __name__ == '__main__':
    main()
