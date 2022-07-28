# import imp
from random import randint
from function import Node, sort_list


def gener_array (n, mx=100):
    return [randint(0, mx) for _ in range(n)]


def arr_to_list(arr):
    guard = Node()
    p = guard
    for item in arr:
        p.next = Node(item)
        p = p.next
    return guard.next


def is_sorted(first):
    p = first
    while p.next is not None:
        if p.val > p.next.val:
            return False
        p = p.next
    return True


def print_list(first):
    while first is not None:
        print(first.val, end=' ')
        first = first.next
    print('')


tab = gener_array(6)
print(tab)
lis = arr_to_list(tab)
print_list(lis)
lis = sort_list(lis)
print_list(lis)
print(is_sorted(lis))
p = Node(7, lis.next)
lis.next = p
print_list(lis)
print(is_sorted(lis))


class TestMin:
    n = 10
    mx = 50

    def test_0(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))
    def test_1(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))
    def test_2(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))
    def test_3(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))
    def test_4(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))

class TestMid:
    n = 200
    mx = 32_769

    def test_0(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))
    def test_1(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))
    def test_2(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))
    def test_3(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))
    def test_4(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))


class TestMax:
    n = 2_000
    mx = 65_536

    def test_0(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))
    def test_1(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))
    def test_2(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))
    def test_3(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))
    def test_4(self):
        assert is_sorted(
            sort_list(
                arr_to_list(gener_array(self.n, self.mx)
                )))


