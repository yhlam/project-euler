"""Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Answer: 6857
"""


import math


def solve():
    MAX_NUM = 600851475143
    SQRT_NUM = int(math.sqrt(MAX_NUM))
    num = MAX_NUM
    i = 2
    while i < SQRT_NUM:
        if num % i == 0 and num != i:
            num /= i
        else:
            i += 1
    return num


if __name__ == '__main__':
    print(solve())
