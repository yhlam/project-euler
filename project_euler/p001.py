"""Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168
"""


def solve():
    sum3 = sum(range(0, 1000, 3))
    sum5 = sum(range(0, 1000, 5))
    sum15 = sum(range(0, 1000, 15))
    sumValue = sum3 + sum5 - sum15
    return sumValue


if __name__ == '__main__':
    print(solve())
