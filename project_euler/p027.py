"""Quadratic primes

Euler published the remarkable quadratic formula:

    n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41,
41^2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for
the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum
number of primes for consecutive values of n, starting with n = 0.

Answer: -59231
"""


from collections import deque
from itertools import count
import math


def solve():
    primes = deque()
    primes.append(2)
    prime_set = set()
    max_prime_evaluated = 2

    def is_prime(n):
        nonlocal max_prime_evaluated, primes, prime_set

        if n < 2:
            return False

        while max_prime_evaluated < n:
            max_prime_evaluated += 1
            max_factor = int(math.sqrt(max_prime_evaluated))
            is_prime_num = True
            for prime_num in primes:
                if prime_num > max_factor:
                    break
                if max_prime_evaluated % prime_num == 0:
                    is_prime_num = False
                    break
            if is_prime_num:
                primes.append(max_prime_evaluated)
                prime_set.add(max_prime_evaluated)

        return n in prime_set

    def quad_func(a, b):
        for x in count():
            yield x * x + a * x + b

    max_count = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            func = quad_func(a, b)
            for count_, value in enumerate(func):
                if not is_prime(value):
                    if count_ > max_count:
                        max_ab = a * b
                        max_count = count_
                    break

    return max_ab


if __name__ == '__main__':
    print(solve())
