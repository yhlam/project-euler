"""10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13. What is the 10001st prime number?

Answer: 104743
"""


import math
from collections import deque


def solve():
    N = 10001
    primes = deque()
    generated = 0
    num = 2
    while generated < N:
        max_factor = int(math.sqrt(num))
        is_prime = True
        for prime_num in primes:
            if prime_num > max_factor:
                break
            if num % prime_num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            generated += 1
        num += 1
    return primes[-1]


if __name__ == '__main__':
    print(solve())
