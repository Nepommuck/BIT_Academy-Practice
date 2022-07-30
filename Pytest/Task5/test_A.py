import pytest
from function import count_chars
import random

# Napisać testy dla funkcji count_chars za pomocą
# markera "parametrize"

# Funkcja count_chars zwraca trzyelementową tablicę
# która zawiera odpowiednio liczbę wystąpień znaku 'a', 'b' i 'c'

# [min_len, max_len, num_of tests]
test_spec = [
    [],
    [5, 20, 5],
    [1_000, 2_000, 5],
]

def gener_test(MN, MX):
    l = random.randint(MN, MX)
    lit = "abc"
    dane = ""
    odp = [0, 0, 0]

    for _ in range(l):
        akt = random.randint(0, 2)
        odp[akt] += 1
        dane += lit[akt]
    
    return (dane, odp)


test_array = [[
    ("abc", [1, 1, 1]),
    ("aaa", [3, 0, 0]),
    ("", [0, 0, 0])]]


for i in range(1, 3):
    test_array.append(
        [gener_test(test_spec[i][0], test_spec[i][1]) for _ in range(test_spec[i][2])]
    )


class TestMin:

    @pytest.mark.parametrize("test_input, expected", test_array[0])
    def test_0(self, test_input, expected):
        assert count_chars(test_input) == expected

 
class TestMid:

    @pytest.mark.parametrize("test_input, expected", test_array[1])
    def test(self, test_input, expected):
        assert count_chars(test_input) == expected


class TestMax:

    @pytest.mark.parametrize("test_input, expected", test_array[2])
    def test_mid(self, test_input, expected):
        assert count_chars(test_input) == expected
