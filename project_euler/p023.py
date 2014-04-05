"""Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

Answer: 4179871
"""


import math


def solve():
    LIMIT = 28123
    abundant = []

    def find_abundant(bound):
        for num in range(2, bound + 1):
            sum = 1
            numSqrt = int(math.sqrt(num))
            for i in range(2, numSqrt + 1):
                if num % i == 0:
                    sum += i
                    pair = num // i
                    if i != pair:
                        sum += pair

            if sum > num:
                abundant.append(num)

    find_abundant(LIMIT)

    size = len(abundant)
    found = [True] * (LIMIT + 1)

    for i in range(size):
        for j in range(i, size):
            num = abundant[i] + abundant[j]
            if num <= LIMIT:
                found[num] = False
            else:
                break

    return sum(x for x in range(1, LIMIT) if found[x])


if __name__ == '__main__':
    print(solve())
