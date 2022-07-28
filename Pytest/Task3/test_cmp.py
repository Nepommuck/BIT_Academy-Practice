from cmath import sqrt
import pytest
import math
from random import randint, random
from cmplex import C

# Testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku


class TestComp:
    def test_0(self):
        a = C(1, 2)
        b = C(1, 3)        
        c = C(2, 5)

        assert a + b == c

    def test_1(self):
        a = C(0, 0)
        b = C(1, 0)        
        c = C(0, 0)

        assert a + b != c

    def test_2(self):
        a = C(-8, -9)
        b = C(2, -2)        
        c = C(-6, -11)

        assert a + b == c
    
    def test_3(self):
        a = C(math.pi - 2, sqrt(2))
        b = C(2, 4)
        c = C(3.14159, sqrt(2) + 4) 

        assert a + b != c 
    
    def test_4(self):
        a = C(math.log(5), 3**2)
        b = C(math.log(3), 4**2)
        c = C(math.log(15), 5**2) 

        assert a + b == c 
