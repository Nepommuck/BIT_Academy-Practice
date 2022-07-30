import pytest

Is_test_okay = True

def f(x):
    return 2 * x


class TestMin:
    def test_0(self):
        if f(2) != 5:
            Is_test_okay = False
        assert f(2) == 5


@pytest.mark.skipif(Is_test_okay, reason="Previous test failed!")
class TestMax:
    def test_A(self):
        assert f(2) == 4

print("aaaaaa")
