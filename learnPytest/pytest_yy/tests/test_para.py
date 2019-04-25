'''
pytest.mark.parametrize()方式进行参数化
测试用例中传入2个参数，year和期望结果，使输入数据与预期结果对应，构造了2组会失败的数据，在执行结果中，可以看到失败原因：
'''
import sys
sys.path.append('.')
import is_leap_year
import pytest

class TestPara():

    # 参数传入year中
    @pytest.mark.parametrize('year, expected', [(1, False), (4, True), (100, False), (400, True), (500, True)])
    def test_is_leap(self, year, expected):
        assert is_leap_year.is_leap_year(year) == expected

    @pytest.mark.parametrize('year, expected', [(0, ValueError), ('-4', TypeError), (-4, ValueError), ('ss', TypeError), (100, ValueError)])
    def test_is_typeerror(self, year,expected):
        if expected == ValueError:
            with pytest.raises(ValueError) as excinfo:
                is_leap_year.is_leap_year(year)
            assert excinfo.type == expected
        else:
            with pytest.raises(TypeError) as excinfo:
                is_leap_year.is_leap_year(year)
            assert excinfo.type == expected
    