import pytest

from api.interface import robot_books


class TestCase:
    @pytest.mark.smoke
    def test_robot_books_case1(self):
        assert robot_books(["56419f31-8245-77a0-682d-f1b1a1bb1383"])['errmsg'] == 'success'
