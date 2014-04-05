"""Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Answer: 142913828922
"""


def solve():
    LIMIT = 2000000
    HALF_LIMIT = LIMIT // 2
    is_prime = [False] + [True] * (HALF_LIMIT - 1)

    total = 2
    for i in range(1, HALF_LIMIT):
        if is_prime[i]:
            num = i + i + 1
            total += num
            base = num + num
            for multiplier in range(num + base, LIMIT, base):
                j = multiplier // 2
                is_prime[j] = False

    return total


if __name__ == '__main__':
    print(solve())
