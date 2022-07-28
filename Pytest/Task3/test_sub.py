from cmplex import C

# Testy sprawdzające odejmowanie liczb zespolonych
# w załączonym pliku

eps = 0.000000001

class TestSub:
    def test_0(self):
        a = C(1, 2)
        b = C(1, 3)        
        rez = a - b

        assert rez.x == 0 and rez.y == -1

    def test_1(self):
        a = C(0, 9)
        b = C(0, 12)        
        rez = a - b

        assert rez.x == 0 and rez.y == -3

    def test_2(self):
        a = C(-8, -9)
        b = C(2, -2)        
        rez = a - b

        assert rez.x == -10 and rez.y == -7

    def test_3(self):
        a = C(0.01, 2.78)
        b = C(-0.12, 96_200)        
        rez = a - b

        assert rez.x == 0.13 and rez.y == -96_197.22

    def test_4(self):
        a = C(1 / 12, 3 / 17)
        b = C(3 / 8, 1 / 13)        
        rez = a - b

        assert rez.x == -7 / 24 and abs(rez.y - 22 / 221) < eps
