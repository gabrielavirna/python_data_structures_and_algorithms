from math import log10, ceil
import random

"""
Multiply two large numbers

-> Iterative algorithm: iteratively multiplying single digit numbers
n digit number requires ~ n^2 multiplication operations (for two 4 digit numbers => 16 multiplication operations)

-> Recursive: Karatsuba algorithm : recursively carries out multiplication operations on progressively smaller inputs
1. decompose a large number into several smaller numbers:
split the number in to two halves: most significant digits| least significant digits.
(four-digit number: 2345, becomes a pair of two-digit numbers, 23 and 45.

General decomposition of any 2 n digit numbers, x and y, where m is any positive integer less than n:

x = 10^m*a + b
y = 10^m*c + d

x*y = (10^m*a + b)(10^m*c + d) = 10^2m*ac + 10^m*ad + 10^m*bc + bd
    = 10^m*ac + 10^2m*(ad + bc) + bd = 10^2m*z_2 + 10^m*z_1 + z_0

z_2 = ac, z_1 = ad + bc, z_0 = bd

(a + b)(c + d) = ac + ad + bc + bd
ac + ad + bc + bd - ac - bd = ad + bc

"""

"""Karatsuba algorithm

1. Recursively calculate ac.
2. Recursively calculate bd.
3. Recursively calculate (a + b)(c + d) and subtract ac and bd."""


def karatsuba(x, y):
    # The base case for recursion
    if x < 10 or y < 10:
        return x * y

    # sets n, the number of digits in the highest input number
    n = max(int(log10(x) + 1), int(log10(y) + 1))   # number of digits in a number : log10(n) + 1

    # rounds up n/2
    n_2 = int(ceil(n / 2.0))

    # adds 1 if n is uneven
    n = n if n % 2 == 0 else n + 1

    # splits the input numbers
    a, b = divmod(x, 10 ** n_2)
    c, d = divmod(y, 10 ** n_2)

    # applies the three recursive steps
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba((a + b), (c + d)) - ac - bd

    # performs the multiplication
    return ((10 ** n) * ac) + bd + ((10 ** n_2) * (ad_bc))

print(karatsuba(23, 45))


##############################################################

def test():
    for i in range(1000):
        x = random.randint(1, 10 ** 5)
        y = random.randint(1, 10 ** 5)
        expected = x * y
        result = karatsuba(x, y)
        if result != expected:
            return "failed"
    return 'ok'

