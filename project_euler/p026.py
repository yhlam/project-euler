"""Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.

Answer: 983
"""


def solve():
    def get_recur_cyc(num):
        dividend = 1
        remainders = []

        while dividend != 0:
            while dividend < num:
                dividend *= 10
                remainders.append(0)

            dividend = dividend % num
            if dividend == 0:
                return 0

            if dividend in remainders:
                size = len(remainders)
                index = remainders.index(dividend)
                return size - index
            else:
                remainders.append(dividend)
                dividend *= 10
        return 0

    maxNum = 0
    maxCycle = 0

    for i in range(1, 1000):
        cycle = get_recur_cyc(i)
        if cycle > maxCycle:
            maxCycle = cycle
            maxNum = i

    return maxNum


if __name__ == '__main__':
    print(solve())
