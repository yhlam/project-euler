"""Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

Answer: 1366
"""


def solve():
    number = 2 ** 1000
    string = str(number)

    sumVal = 0
    for char in string:
        digit = int(char)
        sumVal += digit

    return sumVal


if __name__ == '__main__':
    print(solve())
