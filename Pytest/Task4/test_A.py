import pytest
from function import square
import random

# 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie


class TestBasic:
    MN = -10
    MX = 10
    def test_0(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a
        
    def test_1(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a

    def test_2(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a

    def test_3(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a

    def test_4(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a


class TestMin:
    MN = -1_000
    MX = 1_000
    def test_0(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a
        
    def test_1(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a

    def test_2(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a

    def test_3(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a

    def test_4(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a

        
class TestMid:
    MN = 10 ** 4
    MX = 10 ** 6
    
    pytest.result = True

    def test_0(self):
        a = random.uniform(self.MN, self.MX)
        pytest.result = pytest.result and square(a) == a * a
        assert square(a) == a * a
        
    def test_1(self):
        a = random.uniform(self.MN, self.MX)
        # pytest.result = pytest.result and square(a) == a * a
        assert square(a) == a * a

    def test_2(self):
        a = random.uniform(self.MN, self.MX)
        # pytest.result = pytest.result and square(a) == a * a
        assert square(a) == a * a

    def test_3(self):
        a = random.uniform(self.MN, self.MX)
        # pytest.result = pytest.result and square(a) == a * a
        assert square(a) == a * a

    def test_4(self):
        a = random.uniform(self.MN, self.MX)
        # pytest.result = pytest.result and square(a) == a * a
        assert square(a) == a * a


@pytest.mark.skipif(not pytest.result, reason="Previous test failed!")
class TestMax:
    MN = 10 ** 12
    MX = 10 ** 13

    def test_0(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a
        
    def test_1(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a

    def test_2(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a

    def test_3(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a

    def test_4(self):
        a = random.uniform(self.MN, self.MX)
        assert square(a) == a * a
