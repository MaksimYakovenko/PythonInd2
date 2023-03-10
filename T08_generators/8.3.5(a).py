# 8.3.5(a)
# a0 = 1
# ak = a(k - 1) * (x^2) / (4 * k ** 2 - 2 * k), k >= 1

import math


def f(x, n):
    a = 1
    k = 1
    while k <= n:
        a = (x ** 2) / (4 * k ** 2 - 2 * k) * a
        k += 1
    return a

def gen(x, n):
    a = 1
    k = 1
    while k <= n:
        yield a
        a = (x ** 2) / (4 * k ** 2 - 2 * k) * a
        k += 1
    yield a

if __name__ == "__main__":
    x = 7
    n = 11
    for i in range(n + 1):
        print(round(f(x, i), 2), end = " ")

    print()
    for item in gen(x, n):
        print(round(item, 2), end = " ")
