import pytest

from function import square
# Napisać cztery testy z dla funckji square dla 0, 1, -1 i 100


class Tests:
    def test_1(self):
        assert square(0) == 0

    def test_2(self):
        assert square(1) == 1

    def test_3(self):
        assert square(-1) == 1

    def test_4(self):
        assert square(100) == 10_000
