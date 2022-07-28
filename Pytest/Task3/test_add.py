import pytest
from random import randint, random
from cmplex import C

# Testy sprawdzające dodawanie liczb zespolonych
# w załączonym pliku

class TestAdd:
    def test_0(self):
        a = C(1, 2)
        b = C(1, 3)        
        rez = a + b

        assert rez.x == 2 and rez.y == 5

    def test_1(self):
        a = C(0, 9)
        b = C(0, 12)        
        rez = a + b

        assert rez.x == 0 and rez.y == 21

    def test_2(self):
        a = C(-8, -9)
        b = C(2, -2)        
        rez = a + b

        assert rez.x == -6 and rez.y == -11

    def test_3(self):
        a = C(0.01, 2.78)
        b = C(-0.12, 96_200)        
        rez = a + b

        assert rez.x == -0.11 and rez.y == 96_202.78

    def test_4(self):
        a = C(1 / 12, 3 / 17)
        b = C(3 / 8, 1 / 13)        
        rez = a + b

        assert rez.x == 11 / 24 and rez.y == 56 / 221