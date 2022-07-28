from cmath import sqrt
import math
from cmplex import C

# Testy sprawdzające mnożenie liczb zespolonych
# w załączonym pliku

class TestMul:
    def test_0(self):
        a = C(1, 2)
        b = C(1, 3)        
        rez = a * b

        assert rez.x == -5 and rez.y == 5

    def test_1(self):
        a = C(0, 9)
        b = C(0, 12)        
        rez = a * b

        assert rez.x == -108 and rez.y == 0

    def test_2(self):
        a = C(1, 0)
        b = C(0, 1)        
        rez = a * b

        assert rez.x == 0 and rez.y == 1

    def test_3(self):
        a = C(1, sqrt(2))
        b = C(1, -sqrt(2))        
        rez = a * b

        assert rez.x == 3 and rez.y == 0

    def test_4(self):
        a = C(5, 12)
        b = C(0, 1)        
        rez = a * b

        assert rez.x == -12 and rez.y == 5