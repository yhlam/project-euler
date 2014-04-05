"""Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?

Answer: 232792560
"""


def solve():
    base = 2520
    num = base
    for i in range(11, 21):
        while True:
            if num % i:
                num += base
            else:
                base = num
                break
    return num


if __name__ == '__main__':
    print(solve())
