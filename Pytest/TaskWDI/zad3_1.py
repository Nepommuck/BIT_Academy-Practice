# Napisać funkcję zamieniającą i ZWRACAJĄCĄ W POSTACI NAPISU liczbę naturalną na system o podstawie 2-16.


def num_into_base(num, base):
    rez = ""
    # digit = "0123456789ABCDEF"
    digit = "0123456789abcdef"
    while num > 0:
        akt = num % base
        rez += digit[akt]
        num //= base
    return rez[::-1]


# for i in range(20):
#     print(i, num_into_base(i, 2))
