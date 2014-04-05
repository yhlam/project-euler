"""Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
    1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are
    1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Answer: 31626
"""


import math


def solve():
    LIMIT = 10000
    sums = [0] * LIMIT

    def sum_divisors(num):
        sum_val = 1
        num_sqrt = int(math.sqrt(num))
        for i in range(2, num_sqrt + 1):
            if num % i == 0:
                sum_val += i
                pair = num // i
                if i != pair:
                    sum_val += pair
        sums[num - 1] = sum_val
        return sum_val

    amicable = 0
    for i in range(2, LIMIT + 1):
        sum_val = sum_divisors(i)
        if sum_val < i:
            pair = sums[sum_val - 1]
            if pair == i:
                amicable += i
                amicable += sum_val
    return amicable


if __name__ == '__main__':
    print(solve())
