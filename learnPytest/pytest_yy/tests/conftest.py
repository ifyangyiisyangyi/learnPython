# conftest.py 记住 他叫conftest.py
import pytest

# 准备测试数据
is_leap = [4, 40, 400, 800, 1996, 2996]
is_not_leap = [1, 100, 500, 1000, 1999, 3000]
is_valueerror = [0, -4, -100, -400, -1996, -2000]
is_typeerror = ['-4', '4', '100', 'ins', '**', '中文']

# params中需要传入list
@pytest.fixture(params=is_leap)
def is_leap_y(request):
    return request.param

@pytest.fixture(params=is_typeerror)
def is_type_error(request):
    return request.param