# def is_prime(x):
#     if x == 0 or x == 1:
#         return False
#     for i in range(2, x):
#         if not x % i:
#             return False
#     return True


def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x < 2 or x % 2 == 0 or x % 3 == 0:
        return False
    
    for i in range(6, int(x ** 0.5) + 2, 6):
        if x % (i-1) == 0 or x % (i+1):
            return False
    return True