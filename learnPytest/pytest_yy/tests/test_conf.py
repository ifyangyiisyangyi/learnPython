'''
参数化数据和用例怎么进行分离呢？可以采用conftest.py文件存储参数化数据和函数，模块下的用例执行时，会自动读取conftest.py文件中的数据
'''
import sys
sys.path.append('.')
import is_leap_year
import pytest

class TestPara():
    def test_is_leap(self, is_leap_y):
        assert is_leap_year.is_leap_year(is_leap_y) == True

    def test_is_typeerror(self, is_type_error):
        with pytest.raises(TypeError):
            is_leap_year.is_leap_year(is_type_error)
        # assert is_leap_year.is_leap_year(is_type_error) == False