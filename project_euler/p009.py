"""Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer: 31875000
"""


import math


def solve():
    for a in range(1, 1000):
        limit = 1000 - 2 * a
        if limit >= 0:
            for b in range(1, limit):
                aSq = a * a
                bSq = b * b
                cSq = aSq + bSq
                c = int(math.sqrt(cSq))
                if c * c == cSq:
                    if a + b + c == 1000:
                        return a * b * c


if __name__ == '__main__':
    print(solve())
