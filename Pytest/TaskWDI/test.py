import pytest
from random import randint
from zad3_1 import num_into_base

digit = "0123456789ABCDEF"
MAX_LEN = 14_000


def gener_test(num_r, base_r):
    base = randint(base_r[0], base_r[1])
    length_r = [num_r[0] // base, num_r[1] // base]
    length = min(
        randint(length_r[0], length_r[1]) + 1,
        MAX_LEN
        )

    output = [randint(0, base - 1) for _ in range(length)]
    if output[0] == 0:
        output[0] = 1

    num = calc_num(output, base)
    snum = ""
    for i in output:
        snum += digit[i]

    return (num, base, snum)


def calc_num(arrnum, base):
    mult = 1
    res = 0
    for dig in arrnum[::-1]:
        res += mult * dig
        mult *= base
    return res


# [(num_range), (base_range)]
test_spec = [
    [],
    # test_Digit
    [(1, 100), (2, 10), 5],
    # test_Letter
    [(10, 100), (11, 16), 10],
    # test_Mid
    [(10_000, 20_000), (2, 16), 5],
    # test_Big
    [(MAX_LEN * 12, MAX_LEN * 16), (12, 16), 3]
]

# test_Basic
test_array = [
    [
        (16, 10, "16"),
        (5, 2, "101"),
        (20, 16, "14"),
        (12, 16, "C"),
        (25, 5, "100")
    ]
]

for i in range(1, len(test_spec)):
    test_array.append([
        (
            gener_test(test_spec[i][0], test_spec[i][1])
        ) for _ in range(test_spec[i][2])
    ])

@pytest.mark.parametrize("test_num, test_base, expected", test_array[0])
def test_Basic(test_num, test_base, expected):
    assert num_into_base(test_num, test_base).upper() == expected


@pytest.mark.parametrize("test_num, test_base, expected", test_array[1])
def test_Digit(test_num, test_base, expected):
    assert num_into_base(test_num, test_base).upper() == expected

@pytest.mark.parametrize("test_num, test_base, expected", test_array[2])
def test_Letter(test_num, test_base, expected):
    assert num_into_base(test_num, test_base).upper() == expected

@pytest.mark.parametrize("test_num, test_base, expected", test_array[3])
def test_Mid(test_num, test_base, expected):
    assert num_into_base(test_num, test_base).upper() == expected

@pytest.mark.parametrize("test_num, test_base, expected", test_array[4])
def test_Big(test_num, test_base, expected):
    assert num_into_base(test_num, test_base).upper() == expected
