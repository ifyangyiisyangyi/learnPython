import pytest
import os
import time


def main():
    now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    report_name = os.getcwd() + '\\report\\' + now + '.html'
    pytest.main(['-v', '--html=' + report_name, '--self-contained-html'])


if __name__ == '__main__':
    main()
