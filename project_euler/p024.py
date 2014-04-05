"""Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?

Answer: 2783915460
"""


def solve():
    NUM = 10
    LIMIT = 1000000

    factorial = [1] * (NUM + 1)
    for i in range(1, NUM + 1):
        factorial[i] = factorial[i - 1] * i

    maxVal = LIMIT
    num = 0

    digits = list(range(NUM))

    for i in range(NUM - 1, -1, -1):
        deduct = factorial[i]
        start = 0
        while maxVal > deduct:
            maxVal -= deduct
            start += 1

        digit = digits[start]
        num = num * 10 + digit

        digits.remove(digit)

    return num


if __name__ == '__main__':
    print(solve())
